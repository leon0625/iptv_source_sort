import re

def is_channel_match(template_name, test_name):
    """
    判断 test_name 是否匹配 template_name，
    利用正则确保匹配完整单词（例如 CCTV1 不匹配 CCTV11，但 CCTV5+ 仍然匹配 CCTV5+）
    """

    pattern = rf'\b{re.escape(template_name)}([\s_\-#\(]|$)'
    return re.search(pattern, test_name, re.IGNORECASE) is not None

# 测试用例
print(is_channel_match("CCTV5", "CCTV5"))   # True
print(is_channel_match("CCTV5", "CCTV5 4K"))   # True
print(is_channel_match("CCTV5", "CCTV5+"))     # False
print(is_channel_match("CCTV5+", "CCTV5+ 1080p")) # True
print(is_channel_match("CCTV5", "CCTV51 HD"))  # False
print(is_channel_match("CCTV5", "CCTV5(1080p"))  # True
