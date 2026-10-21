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


