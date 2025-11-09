from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from dotenv import load_dotenv


load_dotenv()
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(... , description="The sentiment of the feedback text")


parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="clasifie the sentiment of the following feedback text into positive or negative \n{feedback},\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
template="Write an a appropriat response to this postive feedback: {feedback}",
input_variables=["feedback"]
)

prompt3=PromptTemplate(
template="Write an a appropriat response to this negative feedback: {feedback}",
input_variables=["feedback"]
)


classifier_chain = prompt1 | chatmodel | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | chatmodel | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | chatmodel | parser),
    RunnableLambda(lambda x: 'could not find sentiment')
)

chain = classifier_chain | branch_chain
final_output = chain.invoke({"feedback": "im very unhappy with your service"})

print(final_output)
chain.get_graph().print_ascii()