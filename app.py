from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st
import ui

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    # repo_id="MiniMaxAI/MiniMax-M2.5",
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

title_prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest blog titles for {topic}"
)

blog_prompt = PromptTemplate(
    input_variables=['title', 'keywords', 'blog_length'],
    template="Write blog on {title} using {keywords} with {blog_length} words"
)

title_chain = title_prompt | model
blog_chain = blog_prompt | model

ui.setup_page()
# ✅ TABS
tab1, tab2 = st.tabs(["✨ Titles", "📝 Blog"])
# tab1, tab2 = st.tabs(["🎯 Generate Titles", "📝 Generate Blog"])

with tab1:
    ui.title_section(title_chain)

with tab2:
    ui.blog_section(blog_chain)