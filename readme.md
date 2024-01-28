### Document Retrieval with FAISS vectorstore, langchain and OpenAI

This is the repository to my tutorial on YouTube: https://youtu.be/N7TQgp18kA4
It will index your pdf documents from the data directory and store it in faiss_db.

You can then retrieve information from your documents, which will require an OpenAI api key.
You can run the document_chat.py file to query your documents, or run the 
telegram_bot to query them on Telegram. This will require an API token, that you will get
from the BotFather in Telegram.

You can add new documents to your index by placing new pdf files in the new_document directory and
running the add_document.py file.

If you want to run everything on gpu, just install faiss-gpu (you must uninstall faiss-cpu then),
and put the embeddings on the gpu by defining it in the config.yaml

### Getting Started

To get started with The document chat, clone the repository and follow these simple steps:

1. **Upgrade pip**: pip install --upgrade pip

2. **Install Requirements**: enter your api keys in the .env file

3. **Customize config file**: Check the config file and change accordingly to the models you downloaded.

4. **Run file**: run ```python3 create_index.py``` , it will create the FAISS index with all the documents in the data folder

5. **Start Chatting**: ```python3 document_chat.py```


### Changes I made to the code you see in the video

I added a config.yaml file where you can define the huggingface embeddings you want to use, and on which device to run it (cpu or cuda).
Also there is the save_path and index_name for FAISS vectorstore defined.

I added the functions load_db, save_db, load_embeddings and load_config in the utils file, to reduce repetetive code in the other .py files.