import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("docs.json") as f:
    documents = json.load(f)

# Extract text
doc_texts = [doc["content"] for doc in documents]

# Convert documents to embeddings
doc_embeddings = model.encode(doc_texts)

# Retrieve most relevant document
def retrieve_answer(query):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    best_index = similarities.argmax()

    return doc_texts[best_index]