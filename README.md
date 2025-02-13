> 根据订阅的IPTV直播源，下载频道接口列表，然后进行测速和排序，生成一份影视仓可用的直播源    
  
# 使用说明  
`python main.py`运行即可，结果生成在output目录  
  
# 可调参数  
subscribe.txt -- 订阅源  
template.txt -- 感兴趣的频道列表，括号内的为别名（根据频道列表匹配频道）  
  
代码中可调参数：  
* MIN_SPEED - 最低速度  
* MIN_RESOLUTION - 最低分辨率  
* MAX_ITEMS_PER_CHANNEL - 每个频道最大保留条目数  
* BLACKLIST_DOMAINS - 黑名单域名  
  