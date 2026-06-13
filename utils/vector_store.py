import os
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from config import Config

VECTOR_DIR = Config.VECTOR_DIR

os.makedirs(VECTOR_DIR, exist_ok=True)

INDEX_FILE = os.path.join(
    VECTOR_DIR,
    "faiss.index"
)

CHUNKS_FILE = os.path.join(
    VECTOR_DIR,
    "chunks.pkl"
)

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

dimension = 384


def create_index():
    return faiss.IndexFlatL2(dimension)


def load_index():
    if os.path.exists(INDEX_FILE):
        return faiss.read_index(INDEX_FILE)

    return create_index()


def save_index(index):
    faiss.write_index(
        index,
        INDEX_FILE
    )


def load_chunks():
    if os.path.exists(CHUNKS_FILE):
        with open(CHUNKS_FILE, "rb") as f:
            return pickle.load(f)

    return []


def save_chunks(chunks):
    with open(CHUNKS_FILE, "wb") as f:
        pickle.dump(chunks, f)

def add_chunks(chunks):
    """
    Add chunks to FAISS index.
    """

    if not chunks:
        return

    index = load_index()

    stored_chunks = load_chunks()

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    embeddings = embeddings.astype(
        np.float32
    )

    index.add(embeddings)

    stored_chunks.extend(chunks)

    save_index(index)

    save_chunks(stored_chunks)

def search_similar_chunks(
    query,
    k=5
):
    """
    Semantic search.
    """

    index = load_index()

    chunks = load_chunks()

    if (
        index.ntotal == 0
        or
        len(chunks) == 0
    ):
        return []

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = query_embedding.astype(
        np.float32
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []
    seen = set()

    for idx in indices[0]:

        if idx < 0 or idx >= len(chunks):
            continue

        chunk = chunks[idx]

        key = (
            chunk["filename"],
            chunk["page"]
        )

        if key in seen:
            continue

        seen.add(key)

        results.append(chunk)

    return results

def reset_vector_store():
    """
    Delete FAISS data.
    """

    if os.path.exists(INDEX_FILE):
        os.remove(INDEX_FILE)

    if os.path.exists(CHUNKS_FILE):
        os.remove(CHUNKS_FILE)




