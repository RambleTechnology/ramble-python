import os
import csv
import requests
from lxml import etree

# 目标主网址
main_url = "https://lishi.tianqi.com/"

# 设置请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}

if not os.path.exists("city_data.csv"):
    # 获取不同城市对应的网址
    try:
        response = requests.get(url=main_url, headers=headers)
        html = etree.HTML(response.text)

        city_name_list = html.xpath("//td/ul/li/a/text()")
        city_url_list = html.xpath("//td/ul/li/a/@href")

        with open("city_data.csv", mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["城市", "代码"])
            for n, u in zip(city_name_list, city_url_list):
                writer.writerow([n, u.split("/")[0]])
                print(n, u.split("/")[0])
    except Exception as e:
        print(e)

else:
    print("城市数据已存在")
