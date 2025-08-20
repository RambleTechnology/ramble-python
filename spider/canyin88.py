import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin, urlparse
import re

def download_images(url, output_folder="downloaded_images", pattern=None):
    """
    下载指定网页中所有匹配模式的图片
    
    Args:
        url (str): 要爬取的网页URL
        output_folder (str): 图片保存目录
        pattern (str): 图片URL匹配模式(正则表达式)
    """
    # 创建输出目录
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 发送HTTP请求
        print(f"正在获取网页内容: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果请求失败则抛出异常
        
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有图片标签
        img_tags = soup.find_all('img')
        print(f"找到 {len(img_tags)} 个图片标签")
        
        # 下载图片
        downloaded_count = 0
        for i, img_tag in enumerate(img_tags):
            # 优先顺序获取图片链接
            img_url = (
                img_tag.get('src') or
                img_tag.get('data-src') or
                img_tag.get('data-original')
            )
            if not img_url:
                continue

            # 处理协议相对路径
            if img_url.startswith('//'):
                img_url = 'https:' + img_url

            # 转换为绝对URL
            img_url = urljoin(url, img_url)

            # 放宽正则表达式，支持 jpg/jpeg/png，允许带参数
            if pattern and not re.search(pattern, img_url, re.IGNORECASE):
                continue
                
            # 获取图片文件名
            parsed_url = urlparse(img_url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = f"image_{int(time.time())}_{i}.jpg"
                
            # 下载图片
            try:
                print(f"正在下载: {img_url}")
                img_response = requests.get(img_url, headers=headers, timeout=10)
                img_response.raise_for_status()
                
                # 保存图片
                filepath = os.path.join(output_folder, filename)
                with open(filepath, 'wb') as f:
                    f.write(img_response.content)
                
                downloaded_count += 1
                print(f"已保存: {filepath}")
                
            except Exception as e:
                print(f"下载图片失败: {img_url}, 错误: {e}")
                
        print(f"完成! 成功下载 {downloaded_count} 张图片")
        
    except Exception as e:
        print(f"获取网页内容失败: {e}")

if __name__ == "__main__":
    # 目标URL
    target_url = "https://www.canyin88.com/zixun/2024/08/05/95681.html"
    
    # 图片URL模式 (正则表达式)
    # 匹配以 https://img.canyin88.com/redsay/ 开头的图片，支持 jpg/jpeg/png，允许带参数
    image_pattern = r"https://img\.canyin88\.com/article/.*\.(jpg|jpeg|png)(\?.*)?$"
    
    # 下载图片
    download_images(target_url, "restaurant_images", image_pattern)