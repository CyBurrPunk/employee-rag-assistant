from pathlib import Path
from pypdf import PdfReader


DATA_FOLDER = Path("data")


def load_documents():

    documents = []

    pdf_files = DATA_FOLDER.glob("*.pdf")

    for pdf in pdf_files:

        reader = PdfReader(pdf)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        documents.append(
            {
                "file_name": pdf.name,
                "content": text,
            }
        )

    return documents