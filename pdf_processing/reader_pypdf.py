# PDF reading using PyPDF

from pypdf import PdfReader

def get_metadata_pypdf(pdf_path):
    """Get metadata of a PDF using PyPDF."""
    reader = PdfReader(pdf_path)
    return reader.metadata

def get_page_count_pypdf(pdf_path):
    """Get number of pages in a PDF using PyPDF."""
    reader = PdfReader(pdf_path)
    return len(reader.pages)
