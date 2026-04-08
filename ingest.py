from dotenv import load_dotenv
load_dotenv()

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils import clone_repo, read_code_files   # ✅ correct import


def build_vectorstore(repo_url):
    # 1️⃣ Clone repo
    path = clone_repo(repo_url)

    # 2️⃣ Read code
    raw_code = read_code_files(path)

    print("📦 Total code length:", len(raw_code))   # Debug

    # 3️⃣ Safety check
    if not raw_code.strip():
        raise ValueError("❌ No readable code found in repository.")

    # 4️⃣ Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200
    )
    chunks = splitter.split_text(raw_code)

    print("✂️ Total chunks created:", len(chunks))  # Debug

    if not chunks:
        raise ValueError("❌ Chunking failed. No chunks created.")

    # 5️⃣ Embeddings + Vector DB
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # 6️⃣ Save locally
    vectorstore.save_local("code_index")

    return "✅ Vector store created successfully!"