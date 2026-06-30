import streamlit as st

from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.chroma_store import index_chunks
from src.rag_pipeline import ask_question

st.set_page_config(
    page_title="Employee Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------- Header ----------

st.title("🤖 Employee Knowledge Assistant")
st.caption(
    "An AI-powered knowledge assistant built using Retrieval-Augmented Generation (RAG), ChromaDB and Gemini."
)

# ---------- Sidebar ----------

with st.sidebar:

    st.header("📌 About")

    st.write(
        """
Ask questions about company policies using AI.

The assistant retrieves relevant policy documents,
grounds responses using those documents,
and generates answers using Gemini.
"""
    )

    st.divider()

    st.subheader("💡 Sample Questions")

    st.markdown("""
- Can I carry forward annual leave?
- What is the travel reimbursement policy?
- How many sick leaves are allowed?
- How do I reset my password?
- How can I access VPN?
""")

    st.divider()

    st.subheader("⚙️ Tech Stack")

    st.markdown("""
- Streamlit
- ChromaDB
- Gemini 2.5 Flash
- Sentence Transformers
- Python
""")

# ---------- Load KB ----------

@st.cache_resource
def load_knowledge_base():

    documents = load_documents()

    chunks = split_documents(documents)

    collection = index_chunks(chunks)

    return collection


collection = load_knowledge_base()

st.success("✅ Knowledge Base Loaded")

# ---------- Question ----------

question = st.text_input(
    "Ask your question",
    placeholder="Example: Can I carry forward annual leave?"
)

col1, col2 = st.columns([1,6])

with col1:

    ask = st.button("🚀 Ask")

if ask:

    if question.strip():

        with st.spinner("Searching documents and generating answer..."):

            answer, sources = ask_question(
                collection,
                question
            )

        st.divider()

        st.subheader("🤖 Answer")

        st.success(answer)

        st.subheader("📚 Sources")

        for source in sources:

            st.markdown(f"📄 **{source}**")

st.divider()

st.caption(
   "Built by Hrishikesh • Powered by Gemini + ChromaDB + Streamlit"
)