#!/usr/bin/env python3
# pdf.py

from image_resize import *

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import(
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('myfile.pdf')  # rename pdf file to execute
for i, image in enumerate(images):
    fname = 'image' + str(i) + '.png'
    image.save(fname, "PNG")

newsize()
