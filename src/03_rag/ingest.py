"""
Layer 3 — RAG: document ingestion.

Reads documents from data/raw/, splits them into chunks, embeds them,
and stores a vector index in chroma_db/ (excluded from git).

Uncomment the requirements in requirements.txt before running.
"""

import os
from pathlib import Path

# Uncomment when you have installed the RAG dependencies:
# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_anthropic import AnthropicEmbeddings
# from langchain_community.vectorstores import Chroma

RAW_DIR = Path(__file__).parent.parent.parent / "data" / "raw"
DB_DIR = Path(__file__).parent.parent.parent / "chroma_db"

CHUNK_SIZE = 500       # tokens — adjust for your material
CHUNK_OVERLAP = 50


def ingest():
    # TODO: replace with your document type (PDF, TXT, etc.)
    # loader = DirectoryLoader(str(RAW_DIR), glob="**/*.pdf", loader_cls=PyPDFLoader)
    # docs = loader.load()
    # splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    # chunks = splitter.split_documents(docs)
    # vectorstore = Chroma.from_documents(chunks, AnthropicEmbeddings(), persist_directory=str(DB_DIR))
    # vectorstore.persist()
    # print(f"Ingested {len(chunks)} chunks from {len(docs)} documents.")
    print("TODO: uncomment and adapt the ingestion code above.")


if __name__ == "__main__":
    ingest()
