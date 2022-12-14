from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger
import PyPDF2
import os
import getpass


def read_pdf_line(pdf_path = "C:/Users/lenovo/Downloads/pdfs/Holiday List 2023.pdf"):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        pdfReader = PyPDF2.PdfFileReader(pdf_path)
        text = ''
        # creating a page object
        pageObj = pdfReader.getPage(0)
        # extracting text from page
        text = text + pageObj.extractText()
        print(text)


# read_pdf_line()


def merge_files():
    merger = PdfFileMerger(strict=False)
    os.chdir("C:/Users/lenovo/Downloads/")
    print(os.listdir())
    for items in os.listdir():
        if items.endswith(".pdf"):
            merger.append(items)
    merger.write("./final_pdf")


# merge_files()
read_pdf_line(pdf_path="./final_pdf")


def protect_file():
    pdfWriter = PdfFileWriter()
    pdf = PdfFileReader('C:/Users/lenovo/Downloads/extec18.pdf')
    for page in range(pdf.numPages):
        pdfWriter.addPage(pdf.getPage(page))
    password = getpass(prompt='Enter password : ')
    pdfWriter.encrypt(password)
    with open('C:/Users/lenovo/Downloads/Holiday List 2023.pdf', 'r+') as file:
        pdfWriter.write(f)


# protect_file()