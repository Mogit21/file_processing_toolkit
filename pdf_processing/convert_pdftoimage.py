# Conversion using pdf2image

from pdf2image import convert_from_path

def pdf_to_images_pdftoimage(pdf_path, output_folder):
    """Convert PDF to images using pdf2image."""
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f"{output_folder}/page_{i + 1}.png", "PNG")
