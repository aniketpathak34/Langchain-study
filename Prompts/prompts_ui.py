#command to run this file "streamlit run prompts_ui.py"

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)

load_dotenv()

st.header("reasearh tool")
user_input = st.text_input("Enter your reasearch topic")


if st.button("Summarize"):
    result = chatmodel.invoke(user_input)
    st.write(result.content)

