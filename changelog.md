# Changelog

All notable changes to this project will be documented here.

---

## v1.0.0 - Static MVP

### Added

* Initial Streamlit application
* User question input
* Static employee policy responses
* Basic UI

---

## v1.1.0 - PDF Ingestion

### Added

* PDF loading module using PyPDF
* Multi-document ingestion
* Reusable backend module

---

## v1.2.0 - Document Chunking

### Added

* Recursive document chunking
* Chunk overlap
* Modular text splitting pipeline


---

## v1.3.0 - Embeddings & Semantic Retrieval

### Added

- Integrated Sentence Transformers (`all-MiniLM-L6-v2`) to generate semantic embeddings.
- Built a custom semantic retrieval pipeline using cosine similarity.
- Added retrieval testing scripts.
- Continued modularizing the RAG pipeline.

### Learning Outcomes

- Understood semantic embeddings.
- Learned cosine similarity.
- Built retrieval before introducing ChromaDB.

## v1.4.0 - ChromaDB Vector Store Integration

### Added

- Integrated ChromaDB as a persistent vector database for storing document embeddings.
- Replaced manual semantic retrieval with ChromaDB similarity search.
- Added document indexing and retrieval modules with reusable helper functions.
- Persisted embeddings locally to support efficient semantic search across application restarts.

### Learning Outcomes

- Understood the role of vector databases in Retrieval-Augmented Generation (RAG).
- Learned how embeddings are indexed and retrieved using similarity search.
- Explored how metadata can be stored alongside vectors for future filtering and retrieval enhancements.