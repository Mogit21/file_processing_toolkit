# Conversion using PyPDF


from pypdf import PdfWriter, PdfReader

def split_pdf_pypdf(pdf_path, output_folder):
    """Split PDF into separate pages using PyPDF."""
    reader = PdfReader(pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{output_folder}/page_{i + 1}.pdf", "wb") as f:
            writer.write(f)
