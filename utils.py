from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from glob import glob
from tqdm import tqdm
import chromadb
import yaml

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

def load_embeddings(model_name=config["embeddings"]["name"],
                    model_kwargs = {'device': config["embeddings"]["device"]}):
    return HuggingFaceEmbeddings(model_name=model_name, model_kwargs = model_kwargs)

def load_documents(directory : str):
    """Loads all documents from a directory and returns a list of Document objects
    args: directory format = directory/
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = config["TextSplitter"]["chunk_size"], 
                                                   chunk_overlap = config["TextSplitter"]["chunk_overlap"])
    documents = []
    for item_path in tqdm(glob(directory + "*.pdf")):
        loader = PyPDFLoader(item_path)
        documents.extend(loader.load_and_split(text_splitter=text_splitter))

    return documents

def load_db(embeddings, save_path=config["chromadb"]["save_path"], collection_name=config["chromadb"]["collection_name"]):
    persistent_client = chromadb.PersistentClient(save_path)

    langchain_chromadb = Chroma(
        client=persistent_client,
        collection_name=collection_name,
        embedding_function=embeddings,
    )

    return langchain_chromadb