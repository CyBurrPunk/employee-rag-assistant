# Employee Knowledge Assistant (Learning RAG from Scratch)

> A hands-on AI learning project to understand how Retrieval-Augmented Generation (RAG) systems are built by developing an employee knowledge assistant using Python, Streamlit, LangChain, ChromaDB and Google Gemini.

---

## 📌 Project Objective

The objective of this project is to build practical AI Product Management fluency by progressively implementing the core building blocks of modern LLM applications instead of only learning theory.

The final application will allow employees to ask natural language questions about company policies and receive accurate, cited answers from internal documents.

---

## Product Vision

Build an AI-powered Employee Knowledge Assistant capable of:

- Answering employee policy and process questions
- Retrieving information from internal documents instead of relying on model memory
- Providing source citations
- Minimizing hallucinations
- Demonstrating production AI concepts such as RAG, GraphRAG and Agentic AI

---

## 🚀 Learning Progress

| Milestone | Status |
|------------|--------|
| Version 1 – Static Employee Assistant | ✅ |
| Milestone 1 – PDF Loading | ✅ |
| Milestone 2 – Document Chunking | ✅ |
| Milestone 3 – Embedding Generation | ✅ |
| Milestone 4 – Semantic Retrieval (Cosine Similarity) | ✅ |
| Milestone 5 – ChromaDB Vector Store | ⏳ Next |
| Milestone 6 – Gemini RAG Pipeline | ⏳ |
| Milestone 7 – Source Citations | ⏳ |
| Milestone 8 – Evaluation Framework | ⏳ |
| Version 3 – GraphRAG | ⏳ |
| Version 4 – Agentic RAG | ⏳ |

---

# What I Learned

### Version 1

- Built a basic Streamlit application
- Accepted user questions
- Displayed policy responses
- Understood the overall user flow before introducing AI

### Milestone 1

Implemented the document ingestion layer.

Learned:

- Reading PDF files using PyPDF
- Extracting text from multiple documents
- Organizing reusable Python modules
- Separating UI from backend logic
- Preparing documents for downstream AI processing

---

# Project Architecture

```
## 🏗️ Current Architecture


flowchart TD

A[Employee Policy PDFs]

--> B[PDF Loader]

B --> C[Document Chunking]

C --> D[Embedding Generation]

D --> E[Manual Semantic Retrieval]

E --> F[Gemini LLM]

F --> G[Answer with Source Citation]
```

---

# Tech Stack

- Python
- Streamlit
- PyPDF
- LangChain *(Upcoming)*
- ChromaDB *(Upcoming)*
- Google Gemini *(Upcoming)*

---

# Repository Structure

```
employee-rag-assistant/

│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   ├── Leave Policy.pdf
│   ├── Travel Policy.pdf
│   └── IT Policy.pdf
│
├── src/
│   └── pdf_loader.py
│
└── images/
```

---

# Learning Roadmap

- [x] Build MVP
- [x] Read PDF documents
- [ ] Split documents into chunks
- [ ] Generate embeddings
- [ ] Create Vector Database
- [ ] Build Retrieval Pipeline
- [ ] Integrate Gemini
- [ ] Add Source Citations
- [ ] Evaluate AI Responses
- [ ] Implement GraphRAG
- [ ] Build Agentic Workflow

---

# Why I Built This

As a Product Manager transitioning into AI Product Management, I wanted to understand how production LLM applications work beyond prompt engineering. Rather than only studying concepts, I am building each component incrementally to learn retrieval, embeddings, evaluation, and AI system design through hands-on experimentation.

---

## Next Milestone

Implement document chunking to prepare policy documents for semantic retrieval.
