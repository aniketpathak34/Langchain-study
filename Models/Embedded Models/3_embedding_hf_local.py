from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = ["indias capital is delhi",
             "paris is the capital of france", "berlin is the capital of germany"]


result = embedding.embed_documents(documents)

result_query = embedding.embed_query("What is the capital of india?")