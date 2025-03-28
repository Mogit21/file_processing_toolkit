# Conversion using PyMuPDF (fitz)


import fitz  # PyMuPDF

def pdf_to_images_pymupdf(pdf_path, output_folder):
    """Convert PDF to images using PyMuPDF."""
    doc = fitz.open(pdf_path)
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        pix = page.get_pixmap()
        pix.save(f"{output_folder}/page_{page_number + 1}.png")
