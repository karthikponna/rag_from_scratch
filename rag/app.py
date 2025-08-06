import os
from dotenv import load_dotenv

from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_key)

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key, model_name="text-embedding-3-small"
)

# Initialize the Chroma client with persistence
chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name, embedding_function=openai_ef
)

def load_documents_from_directory(directory_path):
    documents = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r', encoding="utf-8") as file:
                documents.append({"id": filename, "text": file.read()})
    
    return documents