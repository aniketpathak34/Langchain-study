from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(
    template="write a detailed report on : {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Summarize the following text in a concise manner: {text}",
    input_variables=["text"]
)


prompt1 = template1.invoke({"topic": "black hole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result = model.invoke(prompt2)
print(result.content)
