import os
from http import HTTPStatus
from dashscope import Application

response = Application.call(
    # 若没有配置环境变量，可用百炼API Key将下行替换为：api_key="sk-xxx"。但不建议在生产环境中直接将API Key硬编码到代码中，以减少API Key泄露风险。
    # api_key=os.getenv("sk-819dab9a82664207b7cb29d120d8e163"),
    api_key="sk-xxx",  # 百炼（https://bailian.console.aliyun.com/?tab=app#/app-center） 左下角 API-Key 
    app_id="a663f6d4b9d94207b203d4631644e288",  # 替换为实际的应用 ID
    prompt="识别图片中的时间，格式要求为2025-09-09  12:01:01，直接输出时间",
    # image_list=["https://imgtu.com/uploads/sniwp19z/20250722172248.png"]   # 识别成功
    # image_list=["https://imgtu.com/uploads/snizcr3v/r-20250722172340.webp"]  # 识别成功
    image_list=["https://imgtu.com/uploads/sny90fko/r-winform_5.webp"]     # 识别失败
)

if response.status_code != HTTPStatus.OK:
    print(f"request_id={response.request_id}")
    print(f"code={response.status_code}")
    print(f"message={response.message}")
    print(
        f"请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code"
    )
else:
    print(response.output.text)
