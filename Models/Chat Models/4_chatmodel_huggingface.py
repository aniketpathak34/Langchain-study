from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)


chatmodel = ChatHuggingFace(llm=llm)

response = chatmodel.invoke("What is the capital of India?")
print(response.content)
