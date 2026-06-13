import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from utils.pdf_utils import extract_text_from_pdf
from utils.chunking import chunk_text

pdf_path = input("PDF path: ")

data = extract_text_from_pdf(pdf_path)

chunks = chunk_text(
    data["pages"],
    filename=os.path.basename(pdf_path)
)

print("Pages:", len(data["pages"]))
print("Chunks:", len(chunks))

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0])