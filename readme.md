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

### Changes I made to the code you see in the video

I added a config.yaml file where you can define the huggingface embeddings you want to use, and on which device to run it (cpu or cuda).
Also there is the save_path and index_name for FAISS vectorstore defined.

I added the functions load_db, save_db, load_embeddings and load_config in the utils file, to reduce repetetive code in the other .py files.