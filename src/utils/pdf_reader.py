from PyPDF2 import PdfReader

def extract_text_from_pdf(path: str) -> str:
    """Extracts all text from a PDF file."""
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        page_content = page.extract_text()
        if page_content:
            text.append(page_content)
    return "\n\n".join(text)
