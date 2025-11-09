from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
Documents = [
    "Virat Kohli is one of India's greatest cricketers.",
    "He is known for his aggressive batting and fitness.",
    "Kohli has broken many records across formats.",
    "He served as the captain of the Indian cricket team."
]


query = "Who is Virat Kohli and what is he known for?"


document_embeddings = embedding.embed_documents(Documents)
query_embedding = embedding.aembed_query(query)

score = cosine_similarity([query_embedding], document_embeddings)[0]

index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(query)
print(Documents[index])
print(f"Score: {score}")
