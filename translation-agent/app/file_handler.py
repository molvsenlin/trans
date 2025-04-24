import fitz  # PyMuPDF
from docx import Document

def extract_text_from_pdf(pdf_file):
    """提取PDF文件中的文本"""
    try:
        doc = fitz.open(pdf_file)
    except Exception as e:
        raise ValueError(f"无法打开PDF文件：{e}")
    text = []
    for page in doc:
        page_text = page.get_text()
        text.append(page_text)
    return "\n".join(text)

def extract_text_from_word(word_file):
    """提取Word文件中的文本"""
    try:
        doc = Document(word_file)
    except Exception as e:
        raise ValueError(f"无法打开Word文件：{e}")
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(paragraphs)