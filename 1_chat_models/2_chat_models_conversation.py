import httpx
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

custom_client = httpx.Client(verify=False)

messages = [
    SystemMessage("You are an expert in Equity markets."),
    HumanMessage("Provide me top 10 stocks in the Nifty 50 index."),
    AIMessage("Sure! Here are the top 10 stocks in the Nifty 50 index: 1. Reliance Industries, 2. HDFC Bank, 3. Infosys, 4. ICICI Bank, 5. Tata Consultancy Services, 6. Hindustan Unilever, 7. State Bank of India, 8. Bajaj Finance, 9. Kotak Mahindra Bank, 10. Bharti Airtel."),
    HumanMessage("Provide me banking sector from the list you have provided."),
]

llm = ChatOpenAI(model="gpt-4o", http_client=custom_client)

try:
  result = llm.invoke(messages)
  print(result.content)
except Exception as e:
    print(f"Error: {e}")
