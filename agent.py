from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import json
load_dotenv()
llm=ChatNVIDIA(model="nvidia/nemotron-3-ultra-550b-a55b")
prob=input('ask!')
response=llm.invoke(prob)
print(response.content)

