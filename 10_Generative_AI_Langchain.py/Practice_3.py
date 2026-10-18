from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

import os 

os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model=ChatGroq(model="openai/gpt-oss-20b")

from langchain_tavily import TavilySearch

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general"
)
print(tavily_search_tool.invoke("What is the current AI news"))

from langchain.tools import tool
@tool("calculator",description="Performs arithmetic calculations. Use this for any math problem.")
def calc(expression:str) -> str:
    """Evaluate Mathematical expressions."""
    return str (eval(expression))

from langchain.agents import create_agent

agent = create_agent(model=model,tools=[tavily_search_tool,calc])
print(create_agent)

user_input= "What is the current AI news for Anthropic and then calculate 5+5"

for step in agent.stream(
    {"messages" : user_input},
    stream_mode="values"
):
    step["messages"][-1].pretty_print()

