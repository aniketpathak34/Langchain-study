from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain.output_parsers import StrcturedOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


