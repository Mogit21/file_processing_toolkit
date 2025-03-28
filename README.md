# file_processing_toolkit

# File Processing Toolkit

A Python toolkit for working with PDFs: extract text, read metadata, and convert files.

## Installation
```sh
pip install file-processing-toolkit
'''

The purpose of this project is to create a toolkit that can be used in different file processing tasks.
Some examples would be:
Extract data from pdf files (text, images or tables) and converting them into other formats, like csv ..etc


Before starting file processing on your files, it would be safer to create a copy of your file and transfer it to the backup_files folder. This will avoid to accidentaly alter the original file.

### Running the Tests

pytest tests/



## Usage:


from file_processing_toolkit.pdf_processing.pdf_extractor import extract_text

text = extract_text("sample.pdf", method="pypdf")
print(text)
## 


## Dependencies and Licenses

This project uses the following libraries:

- **pypdf** (MIT License)
- **pdfplumber** (MIT License)
- **pymupdf** (Mozilla Public License 2.0)
- **pdf2image** (MIT License)

Each library's license can be found at:
- pypdf: https://opensource.org/licenses/MIT
- pdfplumber: https://opensource.org/licenses/MIT
- pymupdf: https://opensource.org/licenses/MPL-2.0
- pdf2image: https://opensource.org/licenses/MIT
