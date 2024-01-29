from utils import load_documents, load_db, load_embeddings
from langchain_core.documents.base import Document

def add_documents(documents: list[Document]):
    db = load_db(embedding_function=load_embeddings())
    db.add_documents(documents)
    print("Documents Added")

def main():
    add_documents(load_documents("new_document/"))

if __name__ == "__main__":
    main()