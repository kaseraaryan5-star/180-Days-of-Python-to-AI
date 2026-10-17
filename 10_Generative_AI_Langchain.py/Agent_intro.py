import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

from langchain.tools import tool

@tool
def get_weather (location:str) -> str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

from langchain.agents import create_agent
from langchain_groq import ChatGroq

agent = create_agent(
    model=ChatGroq(model="openai/gpt-oss-20b"),
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

print(agent)
response = agent.invoke({"messages":[{"role":"user","content":"What is the weather like in Bangalore?"}]})
print(response["messages"][-1].content)




from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="qwen/qwen3.8-27b")

agent = create_agent(
    model = model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)
print(agent)

response = agent.invoke({"messages":[{"role":"user","content":"What is the weather like in Bangalore?"}]})
print(response["messages"][-1].content)

