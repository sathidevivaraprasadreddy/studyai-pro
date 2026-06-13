import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from utils.pdf_utils import (
    extract_text_from_pdf
)

from utils.chunking import (
    chunk_text
)

from utils.vector_store import (
    add_chunks
)

pdf_path = input(
    "PDF path: "
)

print("Extracting...")

data = extract_text_from_pdf(
    pdf_path
)

print("Chunking...")

chunks = chunk_text(
    data["pages"],
    filename=os.path.basename(pdf_path)
)

print(
    f"Chunks created: {len(chunks)}"
)

print("Indexing...")

add_chunks(chunks)

print("Done.")