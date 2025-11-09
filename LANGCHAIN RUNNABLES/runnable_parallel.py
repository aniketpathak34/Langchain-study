from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence, RunnableParallel
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
    template="Generate a tweet about {topic} in a humorous way.",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="generate a linkedin post about the following topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet': RunnableSequence(template1, model, parser),
    'linkedin_post': RunnableSequence(template2, model, parser)
})

result = chain.invoke({"topic": "AI"})
print("\n🤖", result)
