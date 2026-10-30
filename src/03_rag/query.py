"""
Layer 3 — RAG: query pipeline.

Retrieves relevant chunks from the vector store and passes them to the LLM.
This is version 3 in your evaluation comparison.

Run ingest.py first to build the vector store.
"""

import os
from pathlib import Path

# Uncomment when you have installed the RAG dependencies:
# from langchain_community.vectorstores import Chroma
# from langchain_anthropic import AnthropicEmbeddings, ChatAnthropic
# from langchain.chains import RetrievalQA

DB_DIR = Path(__file__).parent.parent.parent / "chroma_db"
MODEL = "claude-opus-4-5"
TOP_K = 5  # number of chunks to retrieve


def build_chain():
    # vectorstore = Chroma(persist_directory=str(DB_DIR), embedding_function=AnthropicEmbeddings())
    # llm = ChatAnthropic(model=MODEL)
    # chain = RetrievalQA.from_chain_type(
    #     llm=llm,
    #     retriever=vectorstore.as_retriever(search_kwargs={"k": TOP_K}),
    #     return_source_documents=True,
    # )
    # return chain
    raise NotImplementedError("TODO: uncomment and adapt the RAG chain above.")


def ask(question: str) -> dict:
    chain = build_chain()
    result = chain({"query": question})
    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result.get("source_documents", [])],
    }


if __name__ == "__main__":
    question = "TODO: replace with one of your evaluation questions"
    result = ask(question)
    print(f"A: {result['answer']}")
    print(f"Sources: {result['sources']}")
