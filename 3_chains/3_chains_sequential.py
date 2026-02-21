import httpx
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

custom_client = httpx.Client(verify=False)

llm = ChatOpenAI(model="gpt-4o", http_client=custom_client)

# Define prompt templates
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)

prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})

# Define a prompt template for translation to French
translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = animal_facts_template | llm | StrOutputParser() | prepare_for_translation | translation_template | llm | StrOutputParser() 

# Run the chain
result = chain.invoke({"animal": "cat", "count": 2})

# Output
print(result)