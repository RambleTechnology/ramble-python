from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://mp.weixin.qq.com/s/H2QC4LKQh4YF1waIICLYLg")

time.sleep(3)  # 等待页面加载

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.find("h2", {"class": "rich_media_title"})
if not title_tag:
    title_tag = soup.find("h1", {"class": "rich_media_title"})
title = title_tag.get_text(strip=True) if title_tag else "无标题"

content_tag = soup.find("div", {"id": "js_content"})
content = content_tag.get_text(separator="\n", strip=True) if content_tag else "无内容"

print("标题：", title)
print("\n内容（前500字）：\n", content[:500])