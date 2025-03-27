from PyPDF2 import PdfReader

with open("camera.pdf", "rb") as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    print("The number of pages is", pdf_reader.numpages)