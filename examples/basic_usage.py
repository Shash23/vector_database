"""
Example usage of the vector database.
"""

from vector_db.embedding import TextEmbedder
from vector_db.storage import VectorStore
from vector_db.search import VectorSearch

def main():
    # Initialize components
    embedder = TextEmbedder()
    store = VectorStore(dimension=384)  # MiniLM-L6-v2 produces 384-dimensional vectors
    search = VectorSearch(store)
    
    # Example documents
    documents = [
        "The quick brown fox jumps over the lazy dog",
        "A fast orange fox leaps over a sleepy canine",
        "The weather is beautiful today",
        "It's raining cats and dogs"
    ]
    
    # Add documents to the store
    for doc in documents:
        # Generate embedding
        embedding = embedder.embed(doc)
        # Store vector with metadata
        store.add(embedding.numpy(), metadata={"text": doc})
    
    # Save the store
    store.save("data/example_store")
    
    # Example search
    query = "fox jumping"
    query_embedding = embedder.embed(query)
    results = search.search(query_embedding.numpy(), top_k=2)
    
    print(f"\nSearch results for: {query}")
    for idx, score, metadata in results:
        print(f"Score: {score:.3f}, Text: {metadata['text']}")

if __name__ == "__main__":
    main() 