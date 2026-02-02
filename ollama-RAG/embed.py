import chromadb

client = chromadb.PersistentClient(path="./db") # Specify the path for persistent storage on local disk
collection = client.get_or_create_collection("docs") # Create or get a collection named "docs"

with open("sourceOfTruth_K8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"]) # Add the document to the collection with a unique ID

print("Embedding stored in Chroma")
