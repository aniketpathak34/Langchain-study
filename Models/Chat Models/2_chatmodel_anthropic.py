from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatAnthropic(model="claude-2")

result = chatmodel.invoke("What is the capital of india?")

print(result)