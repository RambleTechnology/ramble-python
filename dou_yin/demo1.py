import requests
import re
from urllib.parse import urlencode

def get_video_url_by_vid(vid):
    # 抖音视频信息API（示例接口，可能需要根据最新规则调整）
    api_url = "https://www.douyin.com/aweme/v1/aweme/detail/"
    params = {
        "aweme_id": vid,
        "device_platform": "web",
        "os": "web",
        # 以下参数可根据实际请求补充（如cookie、referer等）
        # "cookie": "你的Cookie",
        "referer": "https://www.douyin.com/"
    }
    # 拼接请求参数
    url = f"{api_url}?{urlencode(params)}"
    
    try:
        # 发送请求获取视频信息
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # 解析视频地址（抖音视频地址通常在aweme_detail→video→play_addr中）
            if "aweme_detail" in data and "video" in data["aweme_detail"]:
                video_url = data["aweme_detail"]["video"]["play_addr"]["url_list"][0]
                # 抖音视频地址可能需要解码（部分链接为URL编码）
                video_url = re.sub(r"&amp;", "&", video_url)  # 简单处理编码
                return video_url
            else:
                return "未找到视频信息，可能接口结构更新或权限限制"
        else:
            return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"解析出错：{str(e)}"

# 使用示例
# vid = "7507227785396522303"  # 替换为实际的_vid
vid="7406332208941665563"
video_url = get_video_url_by_vid(vid)
print("真实播放地址：", video_url)