import os
import pytest
from file_processing_toolkit.pdf_processing.pdf_converter import convert_pdf_to_images

TEST_PDF = "tests/sample.pdf"
OUTPUT_FOLDER = "tests/output/"

def test_convert_pdf_to_images():
    convert_pdf_to_images(TEST_PDF, OUTPUT_FOLDER, method="pymupdf")
    assert os.path.exists(os.path.join(OUTPUT_FOLDER, "page_1.png")), "Output image should be created"
