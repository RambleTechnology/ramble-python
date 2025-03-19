import requests
import json


# 封装 POST 请求的函数
def send_post_request(url, data, token=None):
    """
    向指定 URL 发送 POST 请求，数据以 JSON 格式传递，支持添加 token

    :param url: 请求的目标 URL
    :param data: 发送的数据，应该是一个字典
    :param token: 可选的 Authorization token
    :return: 返回响应的 JSON 数据（如果有的话）
    """
    # 设置请求头
    headers = {"Content-Type": "application/json"}

    # 如果传递了 token，添加到 headers 中
    if token:
        headers["token"] = token

    # 发送 POST 请求，自动将 data 转换为 JSON 格式
    response = requests.post(url, headers=headers, json=data)

    # 检查响应状态码
    if response.status_code == 200:
        try:
            # 返回 JSON 响应
            return response.json()
        except ValueError:
            # 如果响应不是 JSON 格式
            print("响应不是有效的 JSON 格式")
            return None
    else:
        # 输出错误信息
        print(f"请求失败，状态码: {response.status_code}")
        return None


# 主程序入口
if __name__ == "__main__":
    # 目标 URL
    url = "http://23.39.1.82:8083/label/aircraft"
    url = "http://23.39.1.82:8088/ngh-smart-ar/label/aircraft"

    # 请求数据
    data = {
        "aircraftId": "50010000001310363000",
        "windowWidth": 1842,
        "windowHeight": 1271,
        "labelTypeLogicIds": ["0011864189488548270080","001902001001","001902001001"],
    }

    # 添加 token (可以通过替换下面的值来使用实际的 token)
    token = "c9a313e5-838c-40aa-a68a-108e627e4fcf"

    # 调用 send_post_request 函数发送请求
    response_data = send_post_request(url, data, token)

    # 打印返回的响应数据
    if response_data:
        print("响应数据:", response_data)
