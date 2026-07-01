# 🤖 Employee Knowledge Assistant (RAG)

An AI-powered Employee Knowledge Assistant built to understand how modern enterprise AI assistants work using **Retrieval-Augmented Generation (RAG)**.

Rather than relying solely on a Large Language Model's pre-trained knowledge, this application retrieves relevant information from company policy documents and uses **Google Gemini** to generate accurate, context-aware responses.

> **Why I built this?**
>
> As a Product Manager, I wanted to move beyond AI theory and understand the building blocks behind products like ChatGPT Enterprise, Notion AI and internal company knowledge assistants. The objective wasn't to become an AI engineer, but to understand the product, architecture and design decisions behind AI-powered experiences.

---

# ✨ Features

- 📄 Upload and process employee policy documents
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered contextual question answering
- 📚 Source document references
- ⚡ Interactive Streamlit interface
- 🗂️ ChromaDB vector database
- 🧠 Google Gemini integration

---

# 🏗️ Solution Architecture

```text
                 Employee Policy PDFs
                           │
                           ▼
                  PDF Loader (PyPDF)
                           │
                           ▼
                   Text Chunking
                           │
                           ▼
              Sentence Embeddings
                           │
                           ▼
             ChromaDB Vector Store
                           │
         Similarity Search (Top-K)
                           │
                           ▼
      Prompt + Retrieved Context
                           │
                           ▼
                 Google Gemini LLM
                           │
                           ▼
              Context-Aware Response
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| LLM | Google Gemini 2.5 Flash |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Document Parsing | PyPDF |
| Version Control | Git & GitHub |

---

# 📚 RAG Concepts Explored

This project helped me understand the complete Retrieval-Augmented Generation pipeline:

- PDF Parsing
- Document Chunking
- Embeddings
- Semantic Search
- Vector Databases
- Similarity Search
- Prompt Engineering
- Context Grounding
- LLM Integration
- Retrieval Pipeline Design

One of my biggest takeaways was that **enterprise AI assistants are not just LLMs—they combine retrieval, context management and generation to produce trustworthy responses.**

---

# 🚀 Development Journey

Instead of building everything at once, I intentionally developed the project milestone by milestone to understand each component.

## ✅ Milestone 1 — Document Processing

Implemented:

- PDF ingestion
- Document parsing
- Text extraction

### Key Learning

LLMs cannot directly understand PDFs. Documents first need to be converted into clean text.

---

## ✅ Milestone 2 — Chunking Strategy

Implemented:

- Text chunking
- Chunk overlap
- Metadata preservation

### Key Learning

Chunk size directly impacts retrieval quality. Poor chunking leads to incomplete or irrelevant answers.

---

## ✅ Milestone 3 — Embeddings

Implemented:

- Sentence Transformer embeddings
- Semantic vector generation

### Key Learning

Embeddings convert text into numerical vectors, enabling semantic search instead of simple keyword matching.

---

## ✅ Milestone 4 — Vector Database

Implemented:

- ChromaDB
- Similarity search
- Metadata indexing

### Key Learning

Vector databases enable efficient retrieval of semantically similar information from large document collections.

---

## ✅ Milestone 5 — Retrieval-Augmented Generation

Implemented:

- Top-K retrieval
- Prompt construction
- Gemini integration

### Key Learning

The quality of retrieved context often has a greater impact on answer quality than the LLM itself.

---

## ✅ Milestone 6 — User Interface

Implemented:

- Streamlit interface
- Interactive Q&A
- Source references

### Key Learning

Trust is an important part of AI products. Showing document sources improves transparency and user confidence.

---

# ⚡ Challenges Faced

Like most learning projects, this wasn't just about writing code.

Some interesting challenges included:

- Understanding the complete RAG pipeline from scratch
- Choosing an appropriate chunking strategy
- Working with vector databases for the first time
- Managing Python dependencies
- Learning Git workflows while building
- Integrating Gemini APIs
- Exploring deployment options for AI applications with limited free cloud resources

Each challenge reinforced that building AI products requires balancing **accuracy, architecture, infrastructure and user experience**, not just selecting the right model.

---

# 💡 Product Management Perspective

This project was built with a Product Manager's mindset.

Rather than focusing purely on model implementation, I explored questions like:

- How can users trust AI-generated answers?
- How should retrieval quality be evaluated?
- What are the trade-offs between accuracy and latency?
- When should AI retrieve information versus relying on model knowledge?
- How should AI explain where its answers come from?

These are product decisions as much as technical ones.

---

# 📂 Repository Structure

```
employee-rag-assistant/
│
├── app.py
├── src/
├── data/
├── images/
├── README.md
├── CHANGELOG.md
└── requirements.txt
```

---

# 🔮 What's Next

This project provided a strong foundation in Retrieval-Augmented Generation.

Next, I plan to explore:

- AI Agents
- Model Context Protocol (MCP)
- Agentic Workflows
- RAG Evaluation
- AI Product Design Patterns
- AI UX & Trust
- Multi-Agent Systems

The goal is not simply to build AI applications, but to become a Product Manager who understands how modern AI products are designed, evaluated and delivered.

---

# 👨‍💻 Author

**Hrishikesh Ghadge**

Product Manager | AI Building & Protoyping | Open for AI PM Opportunites

If you have feedback or suggestions, I'd love to connect and learn from the community
Reach out to me on: ghadgehrishikesh@gmail.com
Linkedin: https://www.linkedin.com/in/ghadgehrishikesh1204/