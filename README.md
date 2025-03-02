# PDF to Word & Word to PDF Converter

This project provides a simple way to convert PDF files into Word (.docx) files and vice versa using Python.

## Features

- Convert **PDF to Word (.docx)** using `pdf2docx`
- Convert **Word (.docx) to PDF** using `docx2pdf`
- Lightweight and easy to use

## Requirements

Make sure you have **Python 3.x** installed. You also need to install the required dependencies:

```bash
pip install pdf2docx docx2pdf
```

## Usage

### Convert PDF to Word

Use the following script to convert a **PDF file** to a **Word (.docx) file**:

```python
from pdf2docx import Converter

old_pdf = "general_information.pdf"  # Input PDF file
new_doc = "general_information.docx"  # Output Word file

obj = Converter(old_pdf)  # Create converter instance
obj.convert(new_doc)  # Perform conversion
obj.close()  # Close converter
```

### Convert Word to PDF

Use the following script to convert a **Word (.docx) file** to a **PDF file**:

```python
from docx2pdf import convert
convert("general_information.docx", "general_information2.pdf")
```

## File Structure

```
📂 PDF-Word-Converter
├── 📄 converter_program.py  # Python script for conversion
├── 📄 README.md  # Project documentation
└── 📄 requirements.txt  # Required dependencies
```

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PDF-Word-Converter.git
   cd PDF-Word-Converter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python converter_program.py
   ```

## License

This project is **open-source** and free to use for personal or commercial projects.

---

**Author:** Awais\
**GitHub:** https\://github.com/Awais-official-Dev

