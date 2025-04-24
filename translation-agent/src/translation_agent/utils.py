# src/translation_agent/utils.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL")

def get_completion(prompt: str, system_message: str, model: str = "openai/gpt-4", temperature: float = 0.3) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "temperature": temperature,
        "top_p": 1,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
    }
    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)
    if response.status_code != 200:
        raise RuntimeError(f"API调用失败，状态码：{response.status_code}，内容：{response.text}")
    return response.json()["choices"][0]["message"]["content"].strip()
