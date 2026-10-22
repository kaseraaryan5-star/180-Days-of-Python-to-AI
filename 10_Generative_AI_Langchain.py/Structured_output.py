# STRUCTURED OUTPUT
#Models can be requested to provide their response in a format matching a given schema . This is useful for ensuring the output can be easily parsed and used in subsequent processing . Langchain supports multiple schema types and methods for enforcing structured output.

# PYDANTIC
# Pydantic models provide the richest features set with field validation, descriptions, and nested sturctured

from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

import os 
from langchain.chat_models import init_chat_model

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b")

from pydantic import BaseModel,Field
class Movie(BaseModel):
    title:str=Field(description="The title of the movie")
    year:int=Field(description="The year the movie was released")
    director:str=Field(desciption="The director of the movie")
    rating:float=Field(description="The movie's rating out of 10")

model_with_structred = model.with_structured_output(
    Movie,
    method="json_schema",
)
print(model_with_structred)

print(model.invoke("Provide the details about the movie Inception"))

print(model_with_structred.invoke("Provide the details about the movie Inception"))



### MESSAGE OUTPUT ALONGSIDE PARSED STRUCUTRE

from pydantic import BaseModel,Field

class Movie(BaseModel):
    """A movie with details"""
    title:str=Field(description="The title of the movie")
    year:int=Field(description="The year the movie was released")
    director:str=Field(description="The director of the movie")
    rating:float=Field(description="The movie's rating out of 10")

model_with_structred = model.with_structured_output(Movie, include_raw=True)

response = model_with_structred.invoke("Provide details about the movie Inception")
print(response)




## NESTED STRUCTURE
from pydantic import BaseModel,Field

class Actor(BaseModel):
    name:str
    role:str

class MovieDetails(BaseModel):
    title:str
    year:int
    cast:list[Actor]
    genre:list[str]
    budget:float | None = Field(None,description="Budget in million USD")

model_with_structred = model.with_structured_output(MovieDetails)

response = model_with_structred.invoke("Provide details about the movie Inception")
print(response)



## TYPEDDICT
from typing_extensions import TypedDict,Annotated

class MovieDict(TypedDict):
    """A movie with details"""
    title:Annotated[str,...,"The title of the movie"]
    year:Annotated[int,...,"The year the movie was released"]
    director:Annotated[str,...,"The director of the movie"]
    rating:Annotated[float,...,"The movie's rating out of 10"]

model_withtypedict=model.with_structured_output(MovieDict)
response=model_withtypedict.invoke("Please provide the details of the movie avengers")
print(response)


class Actor(TypedDict):
    name:str
    role:str

class MovieDetails(TypedDict):
    title:str
    year:int
    cast:list[Actor]
    genre:list[str]
    budget:float | None = Field(None,description="Budget in million USD")

model_with_structred = model.with_structured_output(MovieDetails)

response = model_with_structred.invoke("Provide details about the movie Inception")
print(response)

print(model.profile)




### COMPAIRISION BETWEEN PYDANTIC, TYPEDDICT AND DATACLASSES

##PYDANTIC
from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b")

from pydantic import BaseModel,Field
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    """Contact information for a person"""
    name:str=Field(description="The name of the person")
    email:str=Field(description="The email address of the person")
    phone:str=Field(description="The phone number of the person")

agent=create_agent(
    model=model,
    response_format=ContactInfo
)

result=agent.invoke({
    "messages":[{"role":"user","content":"Extract contact info from : John Doe, john@example.com, (555) 123-4567"}]
})

print(result)


##TYPEDDICT
from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b")

from typing_extensions import TypedDict
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    """Contact information for a person"""
    name:str
    email:str
    phone:str
agent=create_agent(
    model=model,
    response_format=ContactInfo
)

result=agent.invoke({
    "messages":[{"role":"user","content":"Extract contact info from : John Doe, john@example.com, (555) 123-4567"}]
})

print(result)


##DATACLASSES
from dotenv import load_dotenv
load_dotenv("/Users/aryankasera/Desktop/100-Days-AI/.env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:openai/gpt-oss-20b")

from dataclasses import dataclass
from langchain.agents import create_agent

@dataclass
class ContactInfo(BaseModel):
    """Contact information for a person"""
    name:str
    email:str
    phone:str
agent=create_agent(
    model=model,
    response_format=ContactInfo
)

result=agent.invoke({
    "messages":[{"role":"user","content":"Extract contact info from : John Doe, john@example.com, (555) 123-4567"}]
})

print(result)
