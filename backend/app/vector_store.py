import faiss
def storing_into_faiss(chunk_embeddings):
    dimension = chunk_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(chunk_embeddings)