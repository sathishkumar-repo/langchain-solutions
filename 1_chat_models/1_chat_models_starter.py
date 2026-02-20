import httpx
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

custom_client = httpx.Client(verify=False)

# Pass that client into the ChatOpenAI object
llm = ChatOpenAI(
    model="gpt-4o",
    http_client=custom_client
)

try:
    result = llm.invoke("What is the capital of France?")
    print(result.content)
except Exception as e:
    print(f"Error: {e}")