from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
import httpx
import os

custom_client = httpx.Client(verify=False)
load_dotenv()

llm = ChatOpenAI(model="gpt-4o", http_client=custom_client)

chat_history = []

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))

    response = llm.invoke(chat_history)
    
    print(f"AI: {response.content}")
    chat_history.append(AIMessage(content=response.content))

print("---- Message History ----")
print(chat_history)