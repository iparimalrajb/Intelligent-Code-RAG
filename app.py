import streamlit as st
from ingest import build_vectorstore
from rag import load_rag

st.set_page_config(page_title="Intelligent Code RAG", layout="wide")
st.title("Intelligent Code RAG – GitHub Code Explainer & Improver")

## Step 1: Index GitHub Repo
repo = st.text_input("Enter the GitHub Repository URL")

if st.button("Index Repository"):
    if not repo:
        st.warning("Please enter a GitHub repository URL.")
    else:
        with st.spinner("Cloning, chunking, and indexing code..."):
            try:
                msg = build_vectorstore(repo)
                st.success(msg)
            except Exception as e:
                st.error(str(e))

st.divider()

## Step 2: Ask Questions about the repo

query = st.text_area("Ask your question about this Repository")

if st.button("Ask"):
    if not query:
        st.warning("Please enter your question.")
    else:
        with st.spinner("Thinking..."):
            try:
                rag = load_rag()
                response = rag.invoke(query)
                st.subheader("Answer")
                st.write(response.content)
            except Exception as e:
                st.error(str(e))