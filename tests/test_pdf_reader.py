import os
import pytest
from file_processing_toolkit.pdf_processing.pdf_reader import get_page_count

# Sample test PDF file
TEST_PDF = "tests/sample.pdf"

def test_get_page_count():
    pages = get_page_count(TEST_PDF, method="pypdf")
    assert pages > 0, "Page count should be greater than zero"
