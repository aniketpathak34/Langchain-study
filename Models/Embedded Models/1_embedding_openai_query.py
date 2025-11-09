from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

OpenAIEmbeddings_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

OpenAIEmbeddings_model.embed_query("What is the capital of india?")

print(OpenAIEmbeddings_model)