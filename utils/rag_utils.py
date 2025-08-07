import os
from PyPDF2 import PdfReader

def load_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = " ".join([page.extract_text() or "" for page in reader.pages])
    return [text[i:i+500] for i in range(0, len(text), 500)]  # chunking
