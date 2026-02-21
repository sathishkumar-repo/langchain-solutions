import httpx
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

custom_client = httpx.Client(verify=False)

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o", http_client=custom_client)

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)
