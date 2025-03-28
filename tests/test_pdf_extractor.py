import pytest
from file_processing_toolkit.pdf_processing.pdf_extractor import extract_text

TEST_PDF = "tests/sample.pdf"

def test_extract_text_pypdf():
    text = extract_text(TEST_PDF, method="pypdf")
    assert isinstance(text, str)
    assert len(text) > 0, "Extracted text should not be empty"
