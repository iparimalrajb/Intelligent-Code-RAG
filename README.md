# 🧠 Intelligent Code RAG – GitHub Code Explainer & Improver

An AI-powered application that allows users to interact with GitHub repositories using natural language.  
This project uses a Retrieval-Augmented Generation (RAG) pipeline to understand, explain, and suggest improvements for code across an entire repository.

---

## 🚀 Features

- 🔗 Input any public GitHub repository URL  
- 📦 Automatically clones and processes the repository  
- 📄 Supports multiple file formats:
  - Python (`.py`)
  - Jupyter Notebooks (`.ipynb`)
  - Markdown (`.md`)  
- ✂️ Splits code into meaningful chunks  
- 🧠 Converts code into vector embeddings  
- 🔍 Retrieves relevant code using semantic search  
- 🤖 Generates explanations and suggestions using LLM  
- 💬 Simple chatbot interface using Streamlit  

---

## 🏗️ Architecture

```
GitHub Repo URL
      ↓
Clone Repository (GitPython)
      ↓
Read Files (.py, .ipynb, .md)
      ↓
Chunking (LangChain Text Splitter)
      ↓
Embeddings (OpenAI)
      ↓
Vector Store (FAISS)
      ↓
Retriever
      ↓
LLM (OpenAI)
      ↓
Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

### 🔹 AI / ML
- OpenAI (LLM + Embeddings)  
- LangChain (RAG pipeline)  
- FAISS (Vector database)  

### 🔹 Backend
- Python  
- GitPython (Repository cloning)  

### 🔹 Frontend
- Streamlit  

### 🔹 Utilities
- python-dotenv (Environment variable management)  

---

## 📂 Project Structure

```
├── app.py              # Streamlit UI  
├── ingest.py           # Repository ingestion & vector store creation  
├── rag.py              # RAG pipeline (retrieval + generation)  
├── utils.py            # Helper functions  
├── requirements.txt  
├── .env  
└── .gitignore  
```

---

## ⚙️ Installation

```bash
git clone https://github.com/iparimalrajb/Intelligent-Code-RAG.git
cd Intelligent-Code-RAG

conda create -n code_rag python=3.10
conda activate code_rag

pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💬 How to Use

1. Open the Streamlit app in your browser  
2. Paste a GitHub repository URL  
3. Click **Index Repository**  
4. Ask questions about the code  

---

## 📊 Example Queries

- “Explain this repository”  
- “What does this function do?”  
- “Suggest improvements for this code”  
- “Find potential issues in this logic”  
- “Rewrite this code using best practices”  
- “Summarize the repository”  

---

## 🧠 Key Concepts

- Retrieval-Augmented Generation (RAG)  
- Semantic Code Search  
- Vector Embeddings  
- Context-aware Code Understanding  

---

## ⚠️ Limitations

- Large repositories may take time to process  
- Performance depends on chunk size and API latency  
- Requires an OpenAI API key  
- Limited to supported file types (`.py`, `.ipynb`, `.md`)  
- May not capture complex inter-file dependencies perfectly  

---

## 🔮 Future Enhancements

- Support for more programming languages  
- Function-level / AST-based chunking  
- Improved evaluation metrics  
- Response time tracking  
- Multi-repository support  
- Deployment on cloud platforms  

---

## 🎯 Project Summary

Built an end-to-end AI system that ingests GitHub repositories, converts code into embeddings, and enables natural language interaction using a RAG pipeline with OpenAI and FAISS.

---

## 👨‍💻 Author

**Parimalraj B**  
