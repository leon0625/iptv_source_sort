#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import concurrent.futures
import json,os,re,sys,time,subprocess,logging
from urllib.request import urlopen
from urllib.parse import quote

# 配置参数
MIN_SPEED = 1024 * 1024  # 1024 KB/s
MIN_RESOLUTION = (1280, 720)  # 720p
MAX_ITEMS_PER_CHANNEL = 6  # 每个频道最大保留条目数
BLACKLIST_DOMAINS = {"www.freetv.top", "piccpndali.v.myalicdn.com"}  # 黑名单域名

# 日志配置
os.makedirs("output", exist_ok=True) 
logging.basicConfig(
    level=logging.INFO,  # 记录所有级别日志
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("output/run.log", mode = "w", encoding="utf-8"),  # 输出到文件
        logging.StreamHandler()  # 输出到终端
    ]
)

# 编码优先级：数值越高优先级越高
CODEC_PRIORITY = {
    'hevc': 2, 'h265': 2,
    'avc': 1, 'h264': 1
}

def codec_priority(codec):
    """ 返回编码格式的优先级，默认为 0 """
    return CODEC_PRIORITY.get(codec.lower(), 0)

class Downloader:
    def __init__(self, url):
        self.url = url
        self.start_time = time.time()
        self.received = 0
        self.end_time = None

    def get_speed(self):
        if self.end_time and (self.end_time - self.start_time) > 0:
            return self.received / (self.end_time - self.start_time)
        return -1

def downloadTester(downloader: Downloader):
    """ 读取一段数据用于测速，最多运行 5 秒 """
    chunk_size = 10240
    try:
        with urlopen(downloader.url, timeout=5) as resp:
            while time.time() - downloader.start_time < 5:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                downloader.received += len(chunk)
    except:
        downloader.received = -1
    downloader.end_time = time.time()

def getStreamUrls(m3u8_url):
    """ 解析 m3u8 文件，返回所有视频流 URL """
    urls = []
    try:
        prefix = m3u8_url[:m3u8_url.rindex('/') + 1]
        with urlopen(m3u8_url, timeout=3) as resp:
            for line in resp:
                line = line.decode('utf-8').strip()
                if line.startswith('#EXTINF:'):
                    continue
                if line and not line.startswith('#'):
                    # 若为相对路径，则拼接前缀
                    if not line.lower().startswith('http'):
                        line = prefix + line
                    urls.append(line)
    except:
        pass
    return urls

def get_resolution_and_codec(url):
    """ 使用 ffprobe 获取视频分辨率和编码格式 """
    try:
        result = subprocess.run([
            'ffprobe', '-v', 'error', '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height,codec_name',
            '-of', 'json', url
        ], capture_output=True, text=True, timeout=10)
        data = json.loads(result.stdout)
        if 'streams' in data and len(data['streams']) > 0:
            stream = data['streams'][0]
            width = stream.get('width', 0)
            height = stream.get('height', 0)
            codec = stream.get('codec_name', 'unknown')
            return width, height, codec
    except Exception as e:
        # print(e)
        pass
    return 0, 0, 'unknown'

def test_url_speed(channel_name, url):
    """
    测试 URL 的下载速率，获取视频分辨率及编码
    若测速或视频信息获取失败，则返回默认值
    """
    # 黑名单域名过滤
    if any(domain in url for domain in BLACKLIST_DOMAINS):
        return channel_name, url, -1, (0, 0, 'unknown')
    
    # 如果不是 .flv 格式，则解析 m3u8 文件获取流地址
    stream_urls = getStreamUrls(url) if not url.lower().endswith('.flv') else [url]
    if not stream_urls:
        return channel_name, url, -1, (0, 0, 'unknown')
    
    downloader = Downloader(stream_urls[0])
    downloadTester(downloader)
    speed = downloader.get_speed()
    if speed < MIN_SPEED:
        # 如果测速速度低于要求，则不再获取视频信息
        return channel_name, url, speed, (0, 0, 'unknown')
    
    resolution = get_resolution_and_codec(stream_urls[0])
    logging.info(f"Tested {channel_name}({speed/1024/1024:.1f}MB/s,{resolution[0]}x{resolution[1]},{resolution[2]}), {url}")
    return channel_name, url, speed, resolution

def fetch_m3u_urls(subscribe_url, max_retries=3):
    """
    获取订阅 URL 内的 m3u 播放列表内容，
    支持两种格式：
      1. 标准 m3u 格式：#EXTINF:开头记录频道名称，后续行为播放地址
      2. 逗号分隔格式：频道名称,播放地址
    添加最多 3 次重试
    """
    urls = []
    for _ in range(max_retries):
        try:
            encoded_url = quote(subscribe_url, safe=':/?=&')  # 仅对非 ASCII 字符进行编码
            with urlopen(encoded_url, timeout=5) as resp:
                lines = resp.read().decode('utf-8', errors='ignore').strip().split('\n')
                channel_name = None
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#EXTM3U'):
                        continue
                    # m3u 格式中频道信息
                    if line.startswith('#EXTINF:'):
                        parts = line.split(',', 1)
                        if len(parts) > 1:
                            channel_name = parts[1].strip()
                    # 逗号分隔格式
                    elif ',' in line:
                        parts = line.split(',', 1)
                        channel = parts[0].strip()
                        url_line = parts[1].strip()
                        urls.append((channel, url_line))
                    else:
                        urls.append((channel_name, line))
                return urls
        except Exception as e:
            logging.warning(f"{e}")
            logging.warning(f"Failed to fetch {subscribe_url}, {e}, try again...")
            time.sleep(1)
            pass
    if not urls:
        logging.error(f"Failed to fetch {subscribe_url}")
    return urls

def read_file(filename):
    """ 按行读取文件，去掉空行 """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

def parse_template(template_file):
    """
    解析模板文件，格式示例：
    
      频道分组标题,#genre#
      CCTV1(CCTV-1,cctv1)
      CCTV4
      
      其他分组标题,#genre#
      CCTV9
      CCTV10
      
    返回：
      groups: { group_title: [主频道名称, ...] }  —— 顺序与模板中保持一致
      alias_map: { alias(小写): 主频道名称 }
    """
    groups = {}
    alias_map = {}
    current_group = None
    
    with open(template_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # 组标题行
            if line.endswith('#genre#'):
                current_group = line
                groups[current_group] = []
            elif current_group:
                # 检查是否包含别名，形如：CCTV1(CCTV-1,cctv1)
                match = re.match(r"^(.+?)\((.+)\)$", line)
                if match:
                    main_name = match.group(1).strip()
                    aliases = [a.strip() for a in match.group(2).split(',')]
                    groups[current_group].append(main_name)
                    # 建立主名称及所有别名映射（均转换为小写）
                    alias_map[main_name.lower()] = main_name
                    for alias in aliases:
                        alias_map[alias.lower()] = main_name
                else:
                    groups[current_group].append(line)
                    alias_map[line.lower()] = line
    return groups, alias_map

def is_channel_match(template_name, test_name):
    """
    判断 test_name 是否匹配 template_name，
    利用正则确保匹配完整单词（例如 CCTV1 不匹配 CCTV11，但 CCTV5+ 仍然匹配 CCTV5+）
    """
    pattern = rf'\b{re.escape(template_name)}([\s_\-#\(]|$)'
    return re.search(pattern, test_name, re.IGNORECASE) is not None

def txt_to_m3u(txt_path, m3u_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    m3u_content = "#EXTM3U\n"
    current_group = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if ",#genre#" in line:
            current_group = line.split(",#")[0].strip()
            continue
        
        if ",http" in line:
            parts = line.split(",http")
            name = parts[0].strip()
            url = "http" + parts[1].strip()
            
            m3u_content += f"#EXTINF:-1 group-title=\"{current_group}\",{name}\n{url}\n"
    
    with open(m3u_path, "w", encoding="utf-8") as f:
        f.write(m3u_content)
    

def main():
    subscribe_file = 'subscribe.txt'
    template_file = 'template.txt'
    
    subscribe_urls = read_file(subscribe_file)
    template_groups, alias_map = parse_template(template_file)
    
    # 从所有订阅地址中并发获取 m3u 条目
    m3u_entries = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(fetch_m3u_urls, url): url for url in subscribe_urls}
        for future in concurrent.futures.as_completed(futures):
            m3u_entries.extend(future.result())
    
    logging.info("all url fetched, count: %d", len(m3u_entries))
    
    # 根据模板对 m3u_entries 进行过滤：
    # 如果条目的频道名称中包含模板中某个名称或别名的完整单词，则归入该分组
    filtered_entries = {group: [] for group in template_groups}
    for entry_name, url in m3u_entries:
        if entry_name:
            matched_channel = None
            for alias, main_name in alias_map.items():
                if is_channel_match(alias, entry_name):
                    matched_channel = main_name
                    break
            if matched_channel:
                for group, channels in template_groups.items():
                    if matched_channel in channels:
                        filtered_entries[group].append((matched_channel, url))
    
    # 对所有分组中的 URL 进行去重，构建 url_to_groups 映射
    # url_to_groups: { url: [(group, channel), ...] }
    url_to_groups = {}
    for group, entries in filtered_entries.items():
        for channel, url in entries:
            if url not in url_to_groups:
                url_to_groups[url] = []
            url_to_groups[url].append((group, channel))
    
    # 对所有唯一 URL 并发测速（重复 URL 只测速一次）
    url_test_results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {}
        for url, groups in url_to_groups.items():
            # 传入的频道名称对测速结果不影响，取第一个即可
            rep_channel = groups[0][1]
            future = executor.submit(test_url_speed, rep_channel, url)
            future_to_url[future] = url
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
            except Exception:
                result = (None, url, -1, (0, 0, 'unknown'))
            url_test_results[url] = result

    # 将测速结果分发到各个分组、各个频道，保证同一频道内 URL 去重
    final_results = {}
    for url, group_list in url_to_groups.items():
        # 测速结果为 (tested_channel, url, speed, (width, height, codec))
        _, _, speed, resolution = url_test_results.get(url, (None, url, -1, (0, 0, 'unknown')))
        for group, channel in group_list:
            if group not in final_results:
                final_results[group] = {}
            if channel not in final_results[group]:
                final_results[group][channel] = {}
            # 如果该 URL 已存在则保留测速更好的结果
            if url not in final_results[group][channel]:
                final_results[group][channel][url] = (speed, resolution)
            else:
                old_speed, _ = final_results[group][channel][url]
                if speed > old_speed:
                    final_results[group][channel][url] = (speed, resolution)
    
    # 输出所有测速结果到 all_results.txt
    all_results_filename = "output/all_results.txt"
    with open(all_results_filename, "w", encoding="utf-8") as out_file:
        # 按模板文件中分组顺序输出
        for group in template_groups:
            if group in final_results:
                out_file.write(f"{group}\n")
                # 按模板中频道出现的顺序输出
                for channel in template_groups[group]:
                    if channel in final_results[group]:
                        entries_list = []
                        for url, (speed, (width, height, codec)) in final_results[group][channel].items():
                            entries_list.append((channel, url, speed, (width, height, codec)))
                        # 同一频道内 URL 按速率、分辨率、编码优先级降序排序
                        entries_list.sort(key=lambda x: (
                            -x[2],
                            -x[3][0],
                            -x[3][1],
                            -codec_priority(x[3][2])
                        ))
                        for channel_name, url, speed, (width, height, codec) in entries_list:
                            out_file.write(f"{channel_name},{speed/1024/1024:.1f}MB/s,{width}x{height},{codec},{url}\n")
                out_file.write("\n")
    
    # 输出符合条件的结果（速率 >= MIN_SPEED 且分辨率满足最低要求）到 filtered_results.txt
    filtered_results_filename = "output/result.txt"
    with open(filtered_results_filename, "w", encoding="utf-8") as out_file:
        for group in template_groups:
            if group in final_results:
                out_file.write(f"{group}\n")
                for channel in template_groups[group]:
                    if channel in final_results[group]:
                        entries_list = []
                        for url, (speed, (width, height, codec)) in final_results[group][channel].items():
                            entries_list.append((channel, url, speed, (width, height, codec)))
                        entries_list.sort(key=lambda x: (
                            -x[2],
                            -x[3][0],
                            -x[3][1],
                            -codec_priority(x[3][2])
                        ))
                        # 限制每个频道最大条目数
                        entries_num = 0
                        for channel_name, url, speed, (width, height, codec) in entries_list:
                            if speed >= MIN_SPEED and width >= MIN_RESOLUTION[0] and height >= MIN_RESOLUTION[1] and entries_num < MAX_ITEMS_PER_CHANNEL:
                                out_file.write(f"{channel_name}({speed/1024/1024:.1f}MB_{height}p_{codec}),{url}\n")
                                entries_num += 1
                out_file.write("\n")
        out_file.write(f"更新时间,#genre#\n")
        out_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},http\n\n")
    print(f"Filtered results saved to {filtered_results_filename}")
    txt_to_m3u(filtered_results_filename, 'output/result.m3u')

if __name__ == "__main__":
    main()
