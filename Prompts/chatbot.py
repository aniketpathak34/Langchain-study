from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        break
    response = chatmodel.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ",response.content)

print(chat_history, "===========----------------==============------------======")