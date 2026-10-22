import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b")

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model=model,
    checkpointer=InMemorySaver()
)

#Run with thread id
config = {"configurable":{"thread_id":"test1"}}

from langchain_core.messages import HumanMessage,SystemMessage
response=agent.invoke({"messages":[HumanMessage(content="Hi my name is Aryan!")]},config=config)
print(response)

print(agent.invoke({"messages":[HumanMessage(content="Hi what is my name?")]},config=config))

#Run with thread id
config1 = {"configurable":{"thread_id":"test2"}}

from langchain_core.messages import HumanMessage,SystemMessage
response=agent.invoke({"messages":[HumanMessage(content="Hi my name is Krishna!")]},config=config1)
print(response)

print(agent.invoke({"messages":[HumanMessage(content="Hi what is my name?")]},config=config1))