# Unified interface for PDF metadata & page count

from .reader_pypdf import get_metadata_pypdf, get_page_count_pypdf
from .reader_pdfplumber import get_metadata_pdfplumber, get_page_count_pdfplumber

def get_metadata(pdf_path, method="pypdf"):
    """Get metadata using the specified method."""
    if method == "pypdf":
        return get_metadata_pypdf(pdf_path)
    elif method == "pdfplumber":
        return get_metadata_pdfplumber(pdf_path)
    else:
        raise ValueError("Invalid method! Choose 'pypdf' or 'pdfplumber'.")

def get_page_count(pdf_path, method="pypdf"):
    """Get page count using the specified method."""
    if method == "pypdf":
        return get_page_count_pypdf(pdf_path)
    elif method == "pdfplumber":
        return get_page_count_pdfplumber(pdf_path)
    else:
        raise ValueError("Invalid method! Choose 'pypdf' or 'pdfplumber'.")
