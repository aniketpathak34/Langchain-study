from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a motivational quote about {topic} in a profound way.",
    input_variables=["topic"]
)

def word_counter(text):
    return len(text.split())


parser = StrOutputParser()

quote_generation = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "qoute": RunnablePassthrough(),
    "word count": RunnableLambda(word_counter)
})

final_chain = RunnableSequence(quote_generation, parallel_chain)
output = final_chain.invoke({"topic": "perseverance"})
print("\n🤖", output)