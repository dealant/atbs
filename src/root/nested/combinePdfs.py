'''
Say you have the boring job of merging several dozen PDF documents into a single PDF file. Each of them has a cover sheet as the first page, but you don’t want the cover sheet repeated in the final result. Even though there are lots of free programs for combining PDFs, many of them simply merge entire files together. Let’s write a Python program to customize which pages you want in the combined PDF.
At a high level, here’s what the program will do:
Find all PDF files in the current working directory.
Sort the filenames so the PDFs are added in order.
Write each page, excluding the first page, of each PDF to the output file.
In terms of implementation, your code will need to do the following:
Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
Call Python’s sort() list method to alphabetize the filenames.
Create a PdfFileWriter object for the output PDF.
Loop over each PDF file, creating a PdfFileReader object for it.
Loop over each page (except the first) in each PDF file.
Add the pages to the output PDF.
Write the output PDF to a file named allminutes.pdf.
'''

#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# TODO: Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
# TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()