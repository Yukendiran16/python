from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger
import PyPDF2
import os

pdf_path = "C:/Users/lenovo/Downloads/pdfs/Holiday List 2023.pdf"


def read_pdf_line():
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


# pass the path of the parent_folder
def fetch_all_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            target_files.append(os.path.join(path, name))
    return target_files


# pass the path of the output final file.pdf and the list of paths
def merge_pdf(out_path: str, extracted_files: list[str]):
    merger = PdfFileMerger()

    for pdf in extracted_files:
        merger.append(pdf)

    merger.write(out_path)
    merger.close()


# get a list of all the paths of the pdf
parent_folder_path = 'C:/Users/lenovo/Downloads/pdfs'
output_pdf_path = './final.pdf'

extracted_files = fetch_all_files(parent_folder_path)
# merge_pdf(output_pdf_path, extracted_files)


def add_watermark():

    with open(pdf_path, 'rb') as sample:
        sample_pdf = PdfFileReader(sample)
        with open("C:/Users/lenovo/Downloads/Sample-Watermark.png", "rb") as image:
            sample_image = image.read()
            file = sample_pdf.getPage(0)
            mark = sample_image.getPage(0)
            file.mergePage(mark)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(file)
            with open("output.pdf", 'wb') as output:
                pdf_writer.write(output)


add_watermark()
