from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv() 

prompt = PromptTemplate(
    template="generate 5 creative ideas about this {topic}",
    input_variables=["topic"]
)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | chatmodel | parser

final_output = chain.invoke({"topic": "space exploration"})

print(final_output)

chain.get_graph().print_ascii()
