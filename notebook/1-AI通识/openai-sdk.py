from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ALIYUN")
# print(api_key)

client = OpenAI(
    api_key=api_key,
    base_url="https://maas.qianwenaiapi.com/compatible-mode/v1"
)

response = client.chat.completions.create(model="qwen3.8-max-0902",
                                     messages=[{"role": "system", "content": "你是一个ai助手"},
                                               {"role": "user", "content": "告诉我现在哈尔滨的天气"}],
                                     stream=False,
                                     temperature=0.1,
                                     )
print(response.choices[0].message.content)