import chromadb
chroma_client = chromadb.Client()

# name of the collection
collection_name = "test_collection"

# create collect if not already exists 
collection = chroma_client.get_or_create_collection(collection_name)

# define documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today"},
    {"id": "doc3", "text": "Good bye, see you later!"}
]

# insert the docs into collection 
for doc in documents:
    collection.upsert(ids=doc["id"], documents= [doc["text"]])

# define query
query_text = "Hello, world!"

results = collection.query(
    query_texts=[query_text],
    n_results=3,
)

print(results["documents"][0])

for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    doc_distance = results["distances"][0][idx]

    print(
        f"For the query: {query_text}, \n Found similar document: {document} (ID: {doc_id}, Distance: {doc_distance})"
    )


    