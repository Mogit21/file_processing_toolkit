# PDF reading using pdfplumber

import pdfplumber

def get_metadata_pdfplumber(pdf_path):
    """Get metadata of a PDF using pdfplumber (limited support)."""
    with pdfplumber.open(pdf_path) as pdf:
        return pdf.metadata  # pdfplumber has limited metadata support

def get_page_count_pdfplumber(pdf_path):
    """Get number of pages in a PDF using pdfplumber."""
    with pdfplumber.open(pdf_path) as pdf:
        return len(pdf.pages)
