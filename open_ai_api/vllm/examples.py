# examples.py

from client import client
from config import MODEL_NAME
from config import API_BASE_URL, API_KEY, MODEL_NAME
from utils import print_response
import requests


def example_chat_completion():
    """聊天对话"""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "讲一个冷笑话"}
        ]
    )
    print_response("Chat Completion", response.choices[0].message.content)


def example_completion():
    """普通文本补全"""
    response = client.completions.create(
        model=MODEL_NAME,
        prompt="写一首关于月亮的诗：",
        max_tokens=100
    )
    print_response("Text Completion", response.choices[0].text)


def example_embeddings():
    """生成 Embeddings"""
    response = client.embeddings.create(
        model=MODEL_NAME,
        input="人工智能正在改变世界"
    )
    print_response("Embeddings", response.data[0].embedding[:20])  # 打印前20维


def example_audio_transcription():
    """语音转文本 (需要音频文件)"""
    with open("sample.mp3", "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model=MODEL_NAME,
            file=audio_file
        )
    print_response("Audio Transcription", response.text)


def example_tokenize():
    """调用 vLLM 特有的 /tokenize 接口"""
    response = client.post("/tokenize", json={
        "model": MODEL_NAME,
        "text": "Hello vLLM"
    })
    print_response("Tokenize", response.json())



def example_tokenize():
    """调用 vLLM 特有的 /tokenize 接口"""
    url = f"{API_BASE_URL}/tokenize"
    payload = {
        "model": MODEL_NAME,
        "text": "Hello vLLM"
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Tokenize", response.json())


def example_detokenize():
    """调用 vLLM 特有的 /detokenize 接口"""
    url = f"{API_BASE_URL}/detokenize"
    payload = {
        "model": MODEL_NAME,
        "tokens": [15496, 995, 1047]  # 示例 token id
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Detokenize", response.json())


def example_score():
    """调用 vLLM 特有的 /score 接口"""
    url = f"{API_BASE_URL}/score"
    payload = {
        "model": MODEL_NAME,
        "prompt": "Beijing is the capital of",
        "completion": "China"
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Score", response.json())


def example_rerank():
    """调用 vLLM 特有的 /v1/rerank 接口"""
    url = f"{API_BASE_URL}/v1/rerank"
    payload = {
        "model": MODEL_NAME,
        "query": "deep learning",
        "documents": [
            "Deep learning is a subset of machine learning.",
            "Bananas are yellow."
        ]
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Re-rank", response.json())