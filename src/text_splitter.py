from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:

        split_text = splitter.split_text(doc["content"])

        for chunk in split_text:

            chunks.append(
                {
                    "source": doc["file_name"],
                    "content": chunk
                }
            )

    return chunks