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

# Current Progress

| Version | Status |
|---------|--------|
| Version 1 - Static MVP | ✅ Completed |
| Milestone 1 - PDF Loading | ✅ Completed |
| Milestone 2 - Document Chunking | ⏳ Next |
| Milestone 3 - Embeddings & Vector DB | ⏳ Planned |
| Milestone 4 - Retrieval Pipeline | ⏳ Planned |
| Milestone 5 - Gemini Response Generation | ⏳ Planned |
| Version 3 - RAG Evaluation | ⏳ Planned |
| Version 4 - GraphRAG | ⏳ Planned |
| Version 5 - Agentic RAG | ⏳ Planned |

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
Employee Policies (PDFs)
            │
            ▼
      PDF Loader ✅
            │
            ▼
    Document Chunking
            │
            ▼
       Embeddings
            │
            ▼
     Chroma Vector DB
            │
            ▼
 Retrieve Relevant Chunks
            │
            ▼
 Google Gemini LLM
            │
            ▼
Answer with Source Citation
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
