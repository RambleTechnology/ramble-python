import requests
import re
import os
import time
import random
from io import BytesIO
from PIL import Image
import urllib3

# 关闭 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
]

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://image.baidu.com/",
        "Connection": "keep-alive",
        "Host": "image.baidu.com",
        "Upgrade-Insecure-Requests": "1",
    }

def download_baidu_images(keyword, num_images=6, save_dir='baidu_images'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://image.baidu.com/",
        "Connection": "keep-alive",
    }
    # 可选：设置初始Cookie（如有需要可抓包获取）
    cookies = {
        # "BAIDUID": "xxx",  # 可选，视情况而定
    }
    # 百度图片搜索URL（改为https）
    search_url = "https://image.baidu.com/search/acjson"
    params = {
        "tn": "resultjson_com",
        "logid": "",
        "ipn": "rj",
        "ct": "201326592",
        "is": "",
        "fp": "result",
        "queryWord": keyword,
        "cl": "2",
        "lm": "-1",
        "ie": "utf-8",
        "oe": "utf-8",
        "st": "-1",
        "ic": "0",
        "word": keyword,
        "face": "0",
        "istype": "2",
        "nc": "1",
        "pn": "0",
        "rn": str(num_images * 2),  # 多抓一些，过滤格式
    }
    session = requests.Session()
    try:
        resp = session.get(
            search_url,
            params=params,
            timeout=10,
            verify=False,
            proxies={"http": None, "https": None},
            headers=get_headers()
        )
        resp.encoding = 'utf-8'
    except requests.exceptions.RequestException as e:
        print(f"请求百度图片接口失败: {e}")
        return

    img_urls = []
    try:
        json_data = resp.json()
        data_list = json_data.get('data', [])
        for item in data_list:
            url = item.get('thumbURL')
            if url and url.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                img_urls.append(url)
            if len(img_urls) >= num_images:
                break
    except Exception as e:
        print("解析图片URL失败，返回内容：", resp.text[:500])
        return

    if not img_urls:
        print("未获取到图片URL，请检查关键字或接口返回内容。")
        return

    count = 0
    for idx, url in enumerate(img_urls):
        try:
            # 随机延迟，模拟人工操作
            time.sleep(random.uniform(1.0, 2.5))
            img_resp = session.get(
                url,
                timeout=10,
                verify=False,
                proxies={"http": None, "https": None},
                headers=get_headers()
            )
            img_bytes = img_resp.content
            ext = url.split('.')[-1].lower()
            if ext == 'webp':
                img = Image.open(BytesIO(img_bytes)).convert('RGB')
                save_path = os.path.join(save_dir, f"{keyword}_{idx+1}.png")
                img.save(save_path, 'PNG')
            else:
                if ext not in ['jpg', 'jpeg', 'png']:
                    ext = 'jpg'
                save_path = os.path.join(save_dir, f"{keyword}_{idx+1}.{ext}")
                with open(save_path, 'wb') as f:
                    f.write(img_bytes)
            print(f"已保存图片: {save_path}")
            count += 1
            if count >= num_images:
                break
        except Exception as e:
            print(f"下载图片失败: {url}，原因: {e}")
            continue

if __name__ == "__main__":
    # keyword = input("请输入要搜索的图片关键词：")
    download_baidu_images("自动售货机", num_images=6)
