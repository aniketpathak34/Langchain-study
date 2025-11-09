from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text: \n{text}",
    input_variables=["text"]
)

prompt2=PromptTemplate(
template="Generate 5 short question answer from the following text: \n{text}",
input_variables=["text"]
)

prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into the single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | chatmodel | parser,
    'quiz': prompt2 | chatmodel | parser
})

merge_chain = prompt3 | chatmodel | parser

chain = parallel_chain | merge_chain

final_output = chain.invoke({'text': "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. It encompasses a variety of subfields, including machine learning, natural language processing, computer vision, and robotics. AI systems can analyze data, recognize patterns, make decisions, and improve their performance over time through experience. The applications of AI are vast and include areas such as healthcare, finance, transportation, and entertainment. As AI technology continues to advance, it holds the potential to revolutionize industries and transform the way we live and work."})

print(final_output)
chain.get_graph().print_ascii()