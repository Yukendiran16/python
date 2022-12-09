from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import PyPDF2
import os

# pdf_path = "C:/Users/lenovo/Documents/Holiday List 2023.pdf"
# with open(pdf_path, 'rb') as f:
#     pdf = PdfFileReader(f)
#     pdfReader = PyPDF2.PdfFileReader(pdf_path)
#     text = ''
#     # creating a page object
#     pageObj = pdfReader.getPage(0)
#     # extracting text from page
#     text = text + pageObj.extractText()
#     print(text)
# information = pdf.getDocumentInfo()
# number_of_pages = pdf.getNumPages()
# print(information)

# f_name = os.path.splitext(os.path.basename(pdf_path))[0]
# for page in range(pdf.getNumPages()):
#     pdf_write = PdfFileWriter()
#     # pdf_write.addPage(pdf.getPage(page))
#     output_filename = '{}_page_{}.pdf'.format(
#         f_name, page + 1)
#     print(output_filename)
#     with open(output_filename, 'wb') as out:
#         pdf_write.write(out)
#     print('Created: {}'.format(output_filename))
# pdf = PdfFileReader(pdf_path)


# original_file = r"C:/Users/lenovo/Downloads/Holiday List 2023.pdf"
# watermark = r"C:/Users/lenovo/Downloads/Holiday List 2023.pdf"
# watermarked_file = r"C:/Users/lenovo/Downloads/Holiday List 2023.pdf"
# watermark = PdfFileReader(watermark)
# watermark_page = watermark.getPage(0)
# pdf_read = PdfFileReader(original_file)
# pdf_write = PdfFileWriter()
# for page in range(pdf_read.getNumPages()):
#     pdf_page = pdf_read.getPage(page)
#     pdf_page.mergePage(watermark_page)
#     pdf_write.addPage(pdf_page)
# with open(watermarked_file, 'wb') as fh:
#     pdf_write.write(fh)
#
#
# pdf_read = PdfFileReader(r"C:/Users/lenovo/Documents/Holiday List 2023.pdf")
# pdf_write = PdfFileWriter()
# page1 = pdf_read.getPage(0)
# pdf_write.addPage(page1)
# print(pdf_write)
# with open(r'C:/Users/lenovo/Downloads/sample-pdf-file.pdf', 'ab') as fh:
#     pdf_write.write(fh)
# with open(r'C:/Users/lenovo/Downloads/sample-pdf-file.pdf', 'ab') as fs:
#     pdf_write.write(fs)


def read_pdf(file_name):
    my_absolute_path = os.path.relpath(file_name)
    with open(my_absolute_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(information)


read_pdf("C:/Users/lenovo/Documents/Holiday List 2023.pdf")
