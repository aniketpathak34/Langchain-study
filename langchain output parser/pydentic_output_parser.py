from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from pydantic import BaseModel
from typing import TypedDict, Annotated, Optional

from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: Annotated[str, "The full name of the person"]
    age: Annotated[int, "The age of the person in years"]
    city: Annotated[Optional[str], "The city where the person lives"]


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= "Provide details of a fictional person in the following format:\n{format_instructions}" ,
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
response = chain.invoke({})
print(response, "=================resukt")