import streamlit as st
from utils import create_pdf
import time

def setup_page():
    st.set_page_config(page_title="AI Blog Assistant", page_icon="🤖", layout="centered")

    st.markdown("""
    <style>
    .stTextInput input {
        background-color: #262730;
        color: white;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>🤖 AI Blog Content Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Create High-Quality Blog Content Effortlessly</p>", unsafe_allow_html=True)
    st.divider()


def title_section(title_chain):
    st.subheader("🎯 Generate Titles")

    topic = st.text_input("Enter Topic")

    if st.button("🚀 Generate Titles"):
        if topic:
            with st.spinner("Generating titles..."):
                result = title_chain.invoke({"topic": topic}).content

            st.success("Titles Generated!")

            for line in result.split("\n"):
                if line.strip():
                    st.markdown(f"- {line.strip()}")


def blog_section(blog_chain):
    st.subheader("📝 Generate Blog")

    title = st.text_input("Enter Blog Title")
    keywords = st.text_input("Enter Keywords (comma separated)")
    words = st.slider("Word Count", 100, 1000, 300)

    # 🔥 Generate
    if st.button("✍ Generate Blog"):
        if title:
            with st.spinner("Writing blog..."):
                result = blog_chain.invoke({
                    "title": title,
                    "keywords": keywords,
                    "blog_length": words
                }).content

            # ✅ store blog
            st.session_state["blog"] = result
            st.session_state["stream_done"] = False   # reset streaming flag

    # ✅ Show blog
    if "blog" in st.session_state:
        result = st.session_state["blog"]

        st.success("Blog Generated!")

        placeholder = st.empty()

        # 🔥 STREAM ONLY FIRST TIME
        if not st.session_state.get("stream_done", False):
            streamed_text = ""
            for char in result:
                streamed_text += char
                placeholder.markdown(streamed_text)
                time.sleep(0.002)

            st.session_state["stream_done"] = True
        else:
            # ✅ NO REWRITE → direct show
            placeholder.markdown(result)
        



        # 📋 COPY
        # st.text_area("Copy your blog 👇", result, height=200)

        # 📄 DOWNLOAD
        pdf_file = create_pdf(result)
        with open(pdf_file, "rb") as f:
            st.download_button(
                "📄 Download Blog",
                f,
                file_name="blog.pdf"
            )