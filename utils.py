import pdfplumber
from docx import Document

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def clean_line(line):
    try:
        return line.encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        return ''.join(char for char in line if ord(char) < 65535)

def save_as_docx(text, path):
    doc = Document()
    for line in text.split("\n"):
        safe_line = clean_line(line)
        doc.add_paragraph(safe_line)
    doc.save(path)
