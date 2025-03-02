# Section to convert a PDF file into a Word (.docx) file:
from pdf2docx import Converter  # Importing the Converter class to convert PDF to DOCX

old_pdf = "general_information.pdf"  # Input PDF file name
new_doc = "general_information.docx"  # Output Word file name

obj = Converter(old_pdf)  # Creating an instance of the Converter class
obj.convert(new_doc)  # Converting the PDF file to Word format
obj.close()  # Closing the conversion process after completion


# Section to convert a Word (.docx) file into a PDF file:
from docx2pdf import convert  # Importing the convert function to convert DOCX to PDF

convert("general_information.docx", "general_information2.pdf")  # Converting Word file to PDF format
