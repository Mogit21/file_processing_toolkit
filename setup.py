from setuptools import setup, find_packages

setup(
    name="file_processing_toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pypdf",
        "pdfplumber",
        "pymupdf",
        "pdf2image"
    ],
    entry_points={
        "console_scripts": [
            "file-processing=file_processing_toolkit.main:main"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A toolkit for PDF processing including text extraction, conversion, and metadata retrieval.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/file_processing_toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
