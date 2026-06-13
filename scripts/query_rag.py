import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from agents.retrieval_agent import (
    retrieve_context
)

query = input(
    "Question: "
)

results = retrieve_context(
    query,
    k=5
)

print()

for i, chunk in enumerate(results, 1):

    print(
        f"Result {i}"
    )

    print(
        f"Source: {chunk['filename']}"
    )

    print(
        f"Page: {chunk['page']}"
    )

    print()

    print(
        chunk["text"][:500]
    )

    print(
        "\n" + "=" * 60 + "\n"
    )