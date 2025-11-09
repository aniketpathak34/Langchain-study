from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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

prompot1 = PromptTemplate(
    template="Generate a joke about {topic} in a humorous way in 10 sentence.",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="explain the the joke in 30 sentence: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

joke_generation = RunnableSequence(prompot1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(template2, model, parser)
})

final_chain= RunnableSequence(joke_generation, parallel_chain)

result = final_chain.invoke({"topic": "AI"})
print("\n🤖", result)
