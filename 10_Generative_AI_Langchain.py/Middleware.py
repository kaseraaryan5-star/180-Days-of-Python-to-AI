# Middleware provides a way to more tightly control what happen inside the agent. Middleware is useful for the following:

  # 1.Tracking agent behaviour with logging, analytics, and debugging.
  # 2.Transforming prompts, tool selection and output formatting.
  # 3.Adding retires, fallbacks, and early termination logic.
  # 4.Appling rate limits, guradrails, and PII selection.

import time
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b",max_retries=5)

## SUMMARIZATION MIDDLEWARE

#Automatically summarize conversation history when approaching token limits, preserving recent messages while compressing other context. Summarization is useful for the following:
  # 1.Long-running conversations that exceed context windows.
  # 2.Multi-turn dialogues with extensive history.
  # 3.Application where preserving full conversation context matters.

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage,SystemMessage

#agent with Message based summarization

agent = create_agent(
    model=model,
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("messages",10),
            keep=("messages",4)
        )
    ]
)
print(agent)

#thread id
config = {"configurable":{"thread_id":"test1"}}

#Alterante test data
questions = [
    "What is 2+2?",
    "What is 10*5?",
    "What is 100/4?",
    "What is 15-7?",
    "What is 3*3?",
    "What is 4*4"
]

for q in questions:
    response=agent.invoke({"messages":[HumanMessage(content=q)]},config=config)
    print(f"Messages:{response}")
    print(f"Messages:{len(response['messages'])}")


# TOKEN SIZE
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

@tool
def search_hotels(city :str) -> str:
    """Search hotels - returns long response to use more tokens."""
    return f"""Hotels in {city}:
    1. Grand Hotel - 5 star, 350$/night, spa, pool, gym
    2. City Inn - 4 star, 180$/night, business center
    3. Budget Stay - 3 star, 75$/night, free wifi"""

agent = create_agent(
    model=model,
    tools=[search_hotels],
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("tokens",550),
            keep=("tokens",200)
        )
    ]
)

config = {"configurable":{"thread_id":"test1"}}

# Token Counter 
def count_tokens(messages):
    total_charges = sum(len(str(m.content))for m in messages)
    return total_charges // 4.     # 4 charges = 1 token

# Run test 
cities = ["Paris","London","Tokyo","New York","Dubai","Singapore"]

for city in cities:
    response = agent.invoke(
        {"messages":[HumanMessage(content=f"Find hotels in {city}")]},
        config=config
    )

    tokens = count_tokens(response["messages"])
    print(f"{city}: ~{tokens} tokens,{len(response['messages'])} messages")
    print(f"{(response['messages'])}")



# FRACTION
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

@tool
def search_hotels(city :str) -> str:
    """Search hotels."""
    return f"Hotels in {city}: Grand Hotel $350, City Inn $180, Budget Stay $75"

# Low fraction for testing !
agent = create_agent(
    model=model,
    tools=[search_hotels],
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("fraction",0.005),    #0.5% = ~640 tokens
            keep=("fraction",0.002),       #0.2% = ~256 tokens
        )
    ]
)

config= {"configurable" : {"thread_id" : "test-1"}}

# Token Counter
def count_tokens(messages):
    return sum(len(str(m.content))for m in messages) // 4

# Test
cities = ["Paris","London","Tokyo","New York","Dubai","Singapore"]

for city in cities:
    response = agent.invoke(
        {"messages":[HumanMessage(content=f"Hotels in {city}")]},
        config=config
    )

    tokens = count_tokens(response["messages"])
    fraction = tokens/128000
    print(f"{city}: ~{tokens} tokens ({fraction:.4%}),{len(response['messages'])} msgs")

    time.sleep(10)




### HUMAN IN THE LOOP MIDDLEWARE 
# Pause agent exection for human approval, editing, or rejection of tool calls before they execute. Human-in-the-loop is useful for the following:
  # 1.High-stakes operation requiring human approval(e.g.,database writes, financial transction)
  # 2.Compliance workflows where human oversight is mandatory.
  # 3.Long-running conversation where human feedback guides the agent.

from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver

def read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    return f"Email content for ID: {email_id}"

def send_email_tool(recipient: str, subject: str , body: str) -> str:
    """Mock function to send an email"""
    return f"Email sent to {recipient} with subject '{subject}'"

agent = create_agent(
    model=model,
    tools=[read_email_tool,send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "send_email_tool":{
                    "allowed_decisions":["approve","edit","reject"]               
                },
                "read_email_tool":False,
            }
        )
    ]
)
print(agent)

config = {"configurable":{"thread_id":"test-approve"}}

## Step 1 : Request
result = agent.invoke(
    {"messages":[HumanMessage(content="Send email to john@test.com with subject 'Hello' and body 'How are you?'")]},
    config=config
)
print(result)

from langgraph.types import Command

## Step A : Approve
if "__interupt__" in result:
    print("Approving")

    result=agent.invoke(
        Command(
            resume={
                "descisions":[
                    {"type":"approve"}
                ]
            }
        ),
        config=config
    )
    print(f"Result: {result['messages'][-1].content}")

## Step B : Reject
if "__interupt__" in result:
    print("Paused! Approving...")

    result=agent.invoke(
        Command(
            resume={
                "decisions":[
                    {"type":"reject"}
                ]
            }
        ),
        config=config
    )
    print(f"Result: {result['messages'][-1].content}")

## Step C : Editing
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver

def read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    return f"Email content for ID: {email_id}"

def send_email_tool(recipient: str, subject: str , body: str) -> str:
    """Mock function to send an email"""
    return f"Email sent to {recipient} with subject '{subject}'"

agent = create_agent(
    model=model,
    tools=[read_email_tool,send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "send_email_tool":{
                    "allowed_decisions":["approve","edit","reject"]               
                },
                "read_email_tool":False,
            }
        ),
    ],
)
print(agent)

config= {"configurable":{"thread_id":"test-edit"}}

#Step 1 :Request (with wrong info)
result = agent.invoke(
    {"messages":[HumanMessage(content="Send email to wrong@email.com with subject 'Test' and body 'Hello'")]},
    config=config
)
print(result)

#Step 2 : Edit or approve
if "__interupt__" in result:
    print("Paused! Editing...")

    result = agent.invoke(
        Command(
            resume={
                "decisions": [
                    {
                        "type":"edit",
                        "edited_action":{
                            "name":"send_email_tool",
                            "args":{
                                "recipient":"correct@email.com",
                                "subject":"Corrected Subject",
                                "body":"This was edited by human before sending",
                            }
                        }
                    }
                ]
            }
        ),
        config=config
    )
    print(agent)