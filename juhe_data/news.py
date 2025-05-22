import requests
import json


def gold():
    apiUrl = "http://web.juhe.cn/finance/gold/shgold"
    requestParams = {
        "key": getAppkey("黄金数据"),
        "v": "1",
    }

    response = requests.get(apiUrl, params=requestParams)
    if response.status_code == 200:
        responseResult = response.json()
        print(responseResult)
    else:
        print("请求异常")


def news():
    apiUrl = "http://v.juhe.cn/toutiao/index"
    requestParams = {
        "key": getAppkey("新闻头条"),
        "type": "",
        "page": "",
        "page_size": "",
        "is_filter": "",
    }

    response = requests.get(apiUrl, params=requestParams)
    if response.status_code == 200:
        responseResult = response.json()
        print(responseResult)
    else:
        print("请求异常")


def joke():
    apiUrl = "http://v.juhe.cn/joke/content/list"
    requestParams = {
        "key": getAppkey("笑话大全"),
        "sort": "",
        "page": "",
        "pagesize": "",
        "time": "",
    }

    # 发起接口网络请求
    response = requests.get(apiUrl, params=requestParams)

    # 解析响应结果
    if response.status_code == 200:
        responseResult = response.json()
        # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
        print(responseResult)
    else:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print("请求异常")


def getAppkey(type):
    try:
        # 打开并加载 JSON 文件
        with open(
            "E:\RedMi_E盘_person\code\Python\聚合数据AppKey.json", "r", encoding="utf-8"
        ) as file:
            data = json.load(file)

        for item in data.get("appKeys", []):
            if item.get("type") == type:
                return item.get("value")
        return None
    except FileNotFoundError:
        print(f"文件未找到!")
        return None
    except json.JSONDecodeError:
        print(f"文件的格式无效!")
        return None


if __name__ == "__main__":
    # gold()
    # news()
    joke()
