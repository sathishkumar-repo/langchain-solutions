from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import httpx
import os 

load_dotenv()

custom_client = httpx.Client(verify=False)

llm = ChatOpenAI(model="gpt-4o", http_client=custom_client)

# Example 1: Prompt with Template strings
# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({
#     "tone":"professional",
#     "company":"Google",
#     "position":"Software Engineer",
#     "skill":"Python programming"
# })

# Example 2: Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are a professor who explains about {topic}."),
    ("human", "Tell me top {topic_count} interesting topics."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "quantum physics", "topic_count": 3})


result = llm.invoke(prompt)
print(result)

result = llm.invoke(prompt)

print(result.content)