from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF while preserving page numbers.
    """

    reader = PdfReader(pdf_path)

    pages = []
    full_text = ""

    for page_num, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:
            page_data = {
                "page": page_num + 1,
                "content": text
            }

            pages.append(page_data)

            full_text += text + "\n"

    return {
        "full_text": full_text,
        "pages": pages
    }