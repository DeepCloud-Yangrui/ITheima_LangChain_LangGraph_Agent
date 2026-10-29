from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from openai import base_url

# 1. 加载环境变量
load_dotenv()       # 加载环境变量
qwen_api_key = os.getenv('ALIYUN')


# 2、定义工具
def get_weather(location:str) -> str:
    """
    用来获取指定地点的天气
    :param location:
    :return:
    """
    return f"当前{location}天气晴朗"

# 3. 创建agent
# qwen不在langchin默认的模型列表中，需要先创建model，再创建agent
qwen_model = init_chat_model(
    model='qwen-max',
    model_provider="openai",
    base_url='https://maas.qianwenaiapi.com/compatible-mode/v1',
    api_key=qwen_api_key,
)
agent = create_agent(model=qwen_model, tools=[get_weather], )

# 4.发起调用
# agent.invoke({
#     "message":[
#         {"role":"user","content":"今天深圳天气如何"}
#     ]
# })

response = agent.invoke({'messages': [HumanMessage('今天深圳天气怎样')]})

print(type(response))
print(response['messages'][-1].content)