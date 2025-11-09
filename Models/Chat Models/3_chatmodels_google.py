from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv

chatmodel = ChatGoogleGenerativeAI(model="gemini-pro")
result = chatmodel.invoke("What is the capital of india?")
print(result.content)