from utils.vector_store import (
    search_similar_chunks
)


def retrieve_context(
    query,
    k=5
):
    return search_similar_chunks(
        query,
        k=k
    )