# config.py
import os

API_BASE_URL = "http://192.168.1.103:8000/v1"
MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct-AWQ"
# API_KEY 从环境变量读取
API_KEY = os.getenv("VLLM_API_KEY")

if not API_KEY:
    raise ValueError("❌ 未检测到环境变量 VLLM_API_KEY，请先设置后再运行。")