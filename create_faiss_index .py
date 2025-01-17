import faiss
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
import warnings
warnings.filterwarnings("ignore")

# Set up your OpenAI API key
openai_api_key = "your api key"
# Sample documents with metadata

documents = [
    {"content": "Barack Obama was the US President for 8 years, from 2009 to 2017.", "source": "History Book", "year": 2020, "published_in": "USA"},
    {"content": "He was the 44th President of the United States, serving from 2009 to 2017.", "source": "Government Records", "year": 2017, "published_in": "USA"},
    {"content": "Obama was re-elected for a second term in 2012, so he was President for a total of 8 years.", "source": "News Article", "year": 2012, "published_in": "New York Times"},
    {"content": "The Atlantic Ocean was first explored by the Norse explorer Leif Erikson around 1000 AD.", "source": "History Book", "year": 1990, "published_in": "Norway"},
    # Add more documents as needed
]

# Initialize embeddings model
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Extract content for embeddings
contents = [doc["content"] for doc in documents]

# Generate embeddings for documents
doc_embeddings = embeddings.embed_documents(contents)

# Initialize FAISS index
dimension = len(doc_embeddings[0])
index = faiss.IndexFlatL2(dimension)

# Add embeddings to the index
index.add(np.array(doc_embeddings))

# Save the index
faiss.write_index(index, "faiss_index_1")

# Save documents with metadata
import json
with open("documents.json", "w") as f:
    json.dump(documents, f)

print("Indexing completed and files saved.")
