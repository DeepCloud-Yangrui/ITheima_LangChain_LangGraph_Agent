from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
# print(api_key)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(model="deepseek-flash",
                                     messages=[{"role": "system", "content": "你是一个ai助手"},
                                               {"role": "user", "content": "告诉我现在哈尔滨的天气"}],
                                     stream=False,
                                     temperature=0.1,
                                     )
print(response.choices[0].message.content)