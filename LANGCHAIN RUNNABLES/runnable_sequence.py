from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a funny joke about {topic} in one sentence.",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Explain the following joke in a detailed manner: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()
chain = RunnableSequence(template1, model, parser, template2, model, parser)

result = chain.invoke({"topic": "AI"})
print("\n🤖", result)
