# examples.py

from client import client
from config import MODEL_NAME
from config import API_BASE_URL, API_KEY, MODEL_NAME
from utils import print_response
import requests
import base64


def encode_image(image_path):
    """将图片编码为base64"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"警告: 图片文件未找到 {image_path}")


def example_chat_completion():
    """聊天对话"""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "讲一个冷笑话"},
        ],
    )
    print_response("Chat Completion", response.choices[0].message.content)


def example_chat_completion_2():
    """聊天对话"""
    # 编码图片
    image_data = encode_image("C:\\Users\\cml\\Desktop\\img\\药店\\1.jpeg")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "图片中有药店吗？"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                    },
                ],
            }
        ],
    )
    print_response("Chat Completion", response.choices[0].message.content)


def example_chat_stream():
    stream = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "基于<动枝生乱影，吹花送远香>这两句，你想到了什么，脑海中看到了什么？然后把感受写成一首诗。"}],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)


def example_completion():
    """普通文本补全"""
    response = client.completions.create(
        model=MODEL_NAME, prompt="写一首关于月亮的诗：", max_tokens=100
    )
    print_response("Text Completion", response.choices[0].text)


def example_embeddings():
    """生成 Embeddings"""
    response = client.embeddings.create(model=MODEL_NAME, input="人工智能正在改变世界")
    print_response("Embeddings", response.data[0].embedding[:20])  # 打印前20维


def example_audio_transcription():
    """语音转文本 (需要音频文件)"""
    with open("sample.mp3", "rb") as audio_file:
        response = client.audio.transcriptions.create(model=MODEL_NAME, file=audio_file)
    print_response("Audio Transcription", response.text)


def example_tokenize():
    """调用 vLLM 特有的 /tokenize 接口"""
    response = client.post(
        "/tokenize", json={"model": MODEL_NAME, "text": "Hello vLLM"}
    )
    print_response("Tokenize", response.json())


def example_tokenize():
    """调用 vLLM 特有的 /tokenize 接口"""
    url = f"{API_BASE_URL}/tokenize"
    payload = {"model": MODEL_NAME, "text": "Hello vLLM"}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Tokenize", response.json())


def example_detokenize():
    """调用 vLLM 特有的 /detokenize 接口"""
    url = f"{API_BASE_URL}/detokenize"
    payload = {"model": MODEL_NAME, "tokens": [15496, 995, 1047]}  # 示例 token id
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Detokenize", response.json())


def example_score():
    """调用 vLLM 特有的 /score 接口"""
    url = f"{API_BASE_URL}/score"
    payload = {
        "model": MODEL_NAME,
        "prompt": "Beijing is the capital of",
        "completion": "China",
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
            "Bananas are yellow.",
        ],
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    print_response("Re-rank", response.json())
