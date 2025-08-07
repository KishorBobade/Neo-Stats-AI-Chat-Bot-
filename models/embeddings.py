from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_vector_store(text_chunks):
    vectors = model.encode(text_chunks)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors))
    return index, text_chunks, vectors

def query_vector_store(query, index, text_chunks, vectors, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [text_chunks[i] for i in I[0]]
