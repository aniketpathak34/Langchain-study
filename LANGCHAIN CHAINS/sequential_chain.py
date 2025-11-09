from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


prompt1 = PromptTemplate(
    template="write a detailed report on : {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text in  5 points and a concise manner: {text}",
    input_variables=["text"]
)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt1 | chatmodel | parser | prompt2 | chatmodel | parser

final_output = chain.invoke({"topic": "upemployement in INDIA"})
print(final_output)
chain.get_graph().print_ascii()