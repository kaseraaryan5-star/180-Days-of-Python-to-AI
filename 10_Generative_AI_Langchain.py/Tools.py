import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)

model = init_chat_model("openai/gpt-oss-20b", model_provider="groq")

response = model.invoke("Write an essay on AI")
print(response.text)


## Tools
from langchain.tools import tool

@tool
def get_weather (location:str) -> str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

model_with_tools = model.bind_tools([get_weather])

response = model_with_tools.invoke("What's the weather in Bangalore")
print(response.text)

print(response.tool_calls)


### Tool Execution Loop
# Step 1 : Model generates tool calls
messages = [{"role":"user","content":"What's the weather in Bangalore?"}]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

# Step 2 : Execute tools and collect results
for tool_call in ai_msg.tool_calls:
    #Execute the tool with the generated arguments
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

# Step 3 : Pass results back to model for final response 
final_response = model_with_tools.invoke(messages)
print(final_response.text)