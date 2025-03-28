# Example usage

# Now, you can call the functions with different methods!


from file_processing_toolkit.pdf_processing.pdf_reader import get_page_count
from file_processing_toolkit.pdf_processing.pdf_extractor import extract_text
from file_processing_toolkit.pdf_processing.pdf_converter import convert_pdf_to_images

pdf_file = "sample.pdf"
output_folder = "output_images"

# Get page count
pages = get_page_count(pdf_file, method="pypdf")
print(f"Total Pages: {pages}")

# Extract text using pdfplumber
text = extract_text(pdf_file, method="pdfplumber")
print("Extracted Text:\n", text)

# Convert to images using pymupdf
convert_pdf_to_images(pdf_file, output_folder, method="pymupdf")
print("PDF converted to images successfully!")
