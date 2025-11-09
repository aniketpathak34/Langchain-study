from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatOpenAI(model="gpt-4")

result = chatmodel.invoke("What is the capital of india?")

print(result)