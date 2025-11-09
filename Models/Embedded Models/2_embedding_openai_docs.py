from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

OpenAIEmbeddings_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


document = ["indias capital is delhi", "paris is the capital of france", "berlin is the capital of germany"]

result_query = OpenAIEmbeddings_model.embed_query("What is the capital of india?")

result_document = OpenAIEmbeddings_model.embed_documents(document)

print(str(result_query), str(result_document))