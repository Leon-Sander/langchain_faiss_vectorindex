from utils import load_documents
from add_documents import add_documents

if __name__ == "__main__":
    documents = load_documents("data/")
    add_documents(documents)