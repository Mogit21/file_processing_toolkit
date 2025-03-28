# Unified interface for PDF conversion

from .convert_pymupdf import pdf_to_images_pymupdf
from .convert_pdftoimage import pdf_to_images_pdftoimage
from .convert_pypdf import split_pdf_pypdf

def convert_pdf_to_images(pdf_path, output_folder, method="pymupdf"):
    """Convert PDF to images using the specified method."""
    if method == "pymupdf":
        return pdf_to_images_pymupdf(pdf_path, output_folder)
    elif method == "pdf2image":
        return pdf_to_images_pdftoimage(pdf_path, output_folder)
    else:
        raise ValueError("Invalid method! Choose 'pymupdf' or 'pdf2image'.")

def split_pdf(pdf_path, output_folder, method="pypdf"):
    """Split PDF into individual pages."""
    if method == "pypdf":
        return split_pdf_pypdf(pdf_path, output_folder)
    else:
        raise ValueError("Invalid method! Choose 'pypdf'.")
