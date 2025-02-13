# 简介  
根据订阅的IPTV直播源，下载频道接口列表，然后进行测速和排序，生成一份影视仓可用的直播源    
  
# 使用说明  
`python main.py`运行即可，结果生成在output目录  
结果示例：  
```
📺央视频道,#genre#
CCTV-1(9.5MB_1080p_h264),http://60.172.130.146:352/tsfile/live/0001_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-1(8.9MB_1080p_h264),http://222.65.166.8:9003//hls/1/index.m3u8
CCTV-1(7.5MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0001_1.m3u8
CCTV-1(6.3MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265001.m3u8?cdn=ystenlive
CCTV-1(5.9MB_1080p_h264),http://183.66.15.146:60901/tsfile/live/0001_1.m3u8
CCTV-1(5.3MB_1080p_h264),http://59.39.89.130:60901/tsfile/live/0001_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-2(11.4MB_1080p_h264),http://liqunhui.cn:35455/itv/1000000001000023315.m3u8?cdn=ystenlive
CCTV-2(9.1MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0002_1.m3u8?key=txiptv&playlive=0&authid=0
CCTV-2(6.5MB_1080p_h264),http://home.dzlove.top:35455/itv/1000000001000023315.m3u8?cdn=ystenlive
CCTV-2(6.1MB_1080p_h264),http://221.205.95.209:9003//hls/2/index.m3u8
CCTV-2(4.6MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0002_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-2(3.9MB_1080p_h264),http://218.58.136.82:352/tsfile/live/0002_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-3(10.3MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265003.m3u8?cdn=ystenlive
CCTV-3(5.8MB_1080p_h264),http://221.205.95.209:9003//hls/3/index.m3u8
CCTV-3(4.0MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0003_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-3(3.8MB_1080p_h264),http://183.66.15.146:60901/tsfile/live/0003_1.m3u8?key=txiptv
CCTV-3(3.8MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0003_1.m3u8
CCTV-3(3.7MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0003_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-4(14.3MB_1080p_h264),http://j.x.bkpcp.top/jx/CCTV4HD
CCTV-4(6.5MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265004.m3u8?cdn=ystenlive
CCTV-4(6.1MB_1080p_h264),http://liqunhui.cn:35455/gaoma/cctv4.m3u8
CCTV-4(5.8MB_1080p_hevc),http://lt.hxtre.com:35455/itv/1000000005000265004.m3u8?cdn=ystenlive
CCTV-4(5.2MB_1080p_h264),http://221.205.95.209:9003//hls/4/index.m3u8
CCTV-4(4.2MB_1080p_hevc),http://home.dzlove.top:35455/itv/1000000005000265004.m3u8?cdn=ystenlive
CCTV-5(6.9MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265005.m3u8?cdn=ystenlive
CCTV-5(6.6MB_1080p_h264),http://221.205.95.209:9003//hls/5/index.m3u8
CCTV-5(6.2MB_1080p_hevc),http://lt.hxtre.com:35455/itv/1000000005000265005.m3u8?cdn=ystenlive
CCTV-5(5.9MB_1080p_h264),http://lt.hxtre.com:35455/gaoma/cctv5.m3u8
CCTV-5(5.8MB_1080p_h264),http://111.160.27.70:35793/tsfile/live/1004_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-5(4.1MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0005_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-5+(15.5MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265016.m3u8?cdn=ystenlive
CCTV-5+(6.6MB_1080p_h264),http://221.205.95.209:9003//hls/6/index.m3u8
CCTV-5+(3.9MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0016_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-5+(3.7MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0016_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-5+(3.4MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0016_1.m3u8
CCTV-5+(3.1MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000020505/index.m3u8?channel-id=bestzb&Contentid=1000000001000020505&livemode=1&stbId=3
CCTV-6(9.3MB_1080p_h264),http://222.65.166.8:9003//hls/6/index.m3u8
CCTV-6(6.8MB_1080p_h264),http://221.205.95.209:9003//hls/7/index.m3u8
CCTV-6(6.4MB_1080p_hevc),http://lt.hxtre.com:35455/itv/1000000005000265006.m3u8?cdn=ystenlive
CCTV-6(6.1MB_1080p_h264),http://113.57.111.4:1111/tsfile/live/1005_1.m3u8
CCTV-6(6.1MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265006.m3u8?cdn=ystenlive
CCTV-6(4.7MB_1080p_h264),http://59.39.89.130:60901/tsfile/live/0006_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-8(15.6MB_2160p_hevc),http://home.dzlove.top:35455/gaoma/cctv8k_36m.m3u8
CCTV-8(11.9MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265008.m3u8?cdn=ystenlive
CCTV-8(9.1MB_1080p_h264),http://222.65.166.8:9003//hls/8/index.m3u8
CCTV-8(5.0MB_1080p_h264),http://183.66.15.146:60901/tsfile/live/0008_1.m3u8?key=txiptv
CCTV-8(4.7MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0008_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-8(4.3MB_1080p_h264),http://home.dzlove.top:35455/gaoma/cctv8.m3u8
CCTV-9(17.8MB_1080p_h264),http://j.x.bkpcp.top/jx/CCTV9HD
CCTV-9(8.9MB_1080p_h264),http://222.65.166.8:9003//hls/9/index.m3u8
CCTV-9(8.4MB_1080p_h264),http://183.66.15.146:60901/tsfile/live/0009_1.m3u8?key=txiptv
CCTV-9(5.1MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265009.m3u8?cdn=ystenlive
CCTV-9(4.9MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000014583/index.m3u8?channel-id=bestzb&Contentid=1000000001000014583&livemode=1&stbId=3
CCTV-9(3.8MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0009_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-10(18.3MB_1080p_h264),http://j.x.bkpcp.top/jx/CCTV10HD
CCTV-10(10.1MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265010.m3u8?cdn=ystenlive
CCTV-10(9.6MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0010_1.m3u8?key=txiptv&playlive=0&authid=0
CCTV-10(7.8MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000023734/index.m3u8?channel-id=bestzb&Contentid=1000000001000023734&livemode=1&stbId=3
CCTV-10(4.7MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0010_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-10(4.5MB_1080p_h264),http://221.205.95.209:9003//hls/11/index.m3u8
CCTV-12(33.1MB_1080p_h264),http://j.x.bkpcp.top/jx/CCTV12HD
CCTV-12(9.7MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0012_1.m3u8?key=txiptv&playlive=0&authid=0
CCTV-12(8.9MB_1080p_h264),http://183.66.15.146:60901/tsfile/live/0012_1.m3u8
CCTV-12(8.8MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265012.m3u8?cdn=ystenlive
CCTV-12(6.0MB_1080p_h264),http://221.205.95.209:9003//hls/13/index.m3u8
CCTV-12(4.3MB_1080p_h264),http://home.dzlove.top:35455/gaoma/cctv12.m3u8
CCTV-13(28.3MB_1080p_h264),http://j.x.bkpcp.top/jx/CCTV13HD
CCTV-13(9.8MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0013_1.m3u8?key=txiptv&playlive=0&authid=0
CCTV-13(6.9MB_1080p_h264),http://home.dzlove.top:35455/itv/5000000011000031108.m3u8?cdn=bestzb
CCTV-13(6.0MB_1080p_h264),http://221.205.95.209:9003//hls/14/index.m3u8
CCTV-13(5.7MB_1080p_h264),http://59.39.89.130:60901/tsfile/live/0013_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-13(5.7MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0013_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-15(11.6MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265014.m3u8?cdn=ystenlive
CCTV-15(3.7MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0015_1.m3u8?key=txiptv&playlive=1&authid=0
CCTV-15(3.1MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000002000008163/index.m3u8?channel-id=bestzb&Contentid=1000000002000008163&livemode=1&stbId=3
CCTV-15(1.0MB_1080p_h264),http://218.89.240.144:59901/tsfile/live/0015_1.m3u8

📡卫视频道,#genre#
浙江卫视(61.8MB_1080p_h264),http://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8
浙江卫视(44.8MB_1080p_h264),https://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8
浙江卫视(22.3MB_1080p_h264),http://ali-m-l.cztv.com/channels/lantian/channel01/1080p.m3u8
浙江卫视(16.1MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265031.m3u8?cdn=ystenlive
浙江卫视(10.8MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0124_1.m3u8?key=txiptv&playlive=0&authid=0
浙江卫视(10.3MB_1080p_h264),http://zhfivel02.cztv.com/channel01/1080p.m3u8?auth_key=2524708799-0-0-adde67b1b344fdd5e512f30a4ae31915
湖南卫视(11.2MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0128_2.m3u8?key=txiptv&playlive=0&authid=0
湖南卫视(8.4MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265024.m3u8?cdn=ystenlive
湖南卫视(4.7MB_1080p_hevc),http://home.dzlove.top:35455/itv/1000000005000265024.m3u8?cdn=ystenlive
湖南卫视(3.3MB_1080p_h264),http://113.101.119.26:8090/hls/130/index.m3u8
湖南卫视(3.1MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000009115/index.m3u8?channel-id=bestzb&Contentid=1000000001000009115&livemode=1&stbId=3
湖南卫视(2.8MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0117_2.m3u8?key=txiptv&playlive=1&authid=0
北京卫视(18.2MB_1080p_h264),http://j.x.bkpcp.top/jx/BEIJHD
北京卫视(11.3MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0122_1.m3u8?key=txiptv&playlive=0&authid=0
北京卫视(6.0MB_1080p_hevc),http://home.dzlove.top:35455/itv/1000000005000265027.m3u8?cdn=ystenlive
北京卫视(5.4MB_1080p_h264),https://live-hls-web-ajb.getaj.net/AJB/01.m3u8
北京卫视(3.5MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265027.m3u8?cdn=ystenlive
北京卫视(3.3MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0122_1.m3u8?key=txiptv&playlive=1&authid=0
东方卫视(10.5MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265018.m3u8?cdn=ystenlive
东方卫视(9.1MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0107_1.m3u8?key=txiptv&playlive=0&authid=0
东方卫视(6.1MB_1080p_h264),http://222.174.239.62:352/tsfile/live/0107_1.m3u8?key=txiptv&playlive=1&authid=0
东方卫视(5.8MB_1080p_hevc),http://home.dzlove.top:35455/itv/1000000005000265018.m3u8?cdn=ystenlive
东方卫视(4.9MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000005866/index.m3u8?channel-id=bestzb&Contentid=1000000001000005866&livemode=1&stbId=3
东方卫视(4.1MB_1080p_h264),http://175.18.189.238:9998/tsfile/live/0107_1.m3u8?key=txiptv&playlive=1&authid=0
江苏卫视(13.7MB_1080p_hevc),http://liqunhui.cn:35455/itv/1000000005000265030.m3u8?cdn=ystenlive
江苏卫视(9.6MB_1080p_h264),http://39.164.180.36:19901/tsfile/live/0127_1.m3u8?key=txiptv&playlive=0&authid=0
江苏卫视(6.7MB_1080p_h264),http://182.37.169.94:352/tsfile/live/0127_1.m3u8?key=txiptv&playlive=1&authid=0
江苏卫视(5.0MB_1080p_hevc),http://home.dzlove.top:35455/itv/1000000005000265030.m3u8?cdn=ystenlive
江苏卫视(4.9MB_1080p_h264),http://111.29.9.33:6610/000000001000/1000000001000001828/index.m3u8?channel-id=bestzb&Contentid=1000000001000001828&livemode=1&stbId=3
江苏卫视(4.4MB_1080p_h264),http://113.57.111.4:1111/tsfile/live/1019_1.m3u8

更新时间,#genre#
2025-02-13 11:37:58,http
```
  
# 可调参数  
subscribe.txt -- 订阅源  
template.txt -- 感兴趣的频道列表，括号内的为别名（根据频道列表匹配频道）  
  
代码中可调参数：  
* MIN_SPEED - 最低速度  
* MIN_RESOLUTION - 最低分辨率  
* MAX_ITEMS_PER_CHANNEL - 每个频道最大保留条目数  
* BLACKLIST_DOMAINS - 黑名单域名  
  