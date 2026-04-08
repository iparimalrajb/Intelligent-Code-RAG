import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def load_rag():
    embeddings = OpenAIEmbeddings()

    if not os.path.exists("code_index"):
        raise ValueError("Vector store not found. Please index a repository first.")

    vectordb = FAISS.load_local(
    "code_index",
    embeddings,
    allow_dangerous_deserialization=True
)

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_template("""
You are a senior software engineer and a mentor who is always ready to teach.
Use the following code context to answer the question.
If user asks for improvements, return improved code.

Context:
{context}

Question:
{question}
""")

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return rag_chain