# client.py

from openai import OpenAI
from config import API_BASE_URL, API_KEY, MODEL_NAME


print("API Base:", API_BASE_URL)
print("Model:", MODEL_NAME)
print("API Key 前 8 位:", API_KEY[:8] + "****")

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URL
)
