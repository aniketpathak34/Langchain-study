from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
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

prompt2 = PromptTemplate(
    template="somerize this text in one sentence: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

quote_generation = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 30, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_output_chain = RunnableSequence(quote_generation, branch_chain)


output = final_output_chain.invoke({"topic": "perseverance"})
print("\n🤖", output)