import os
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('myfile.pdf')  # rename any pdf to this to convert
for i, image in enumerate(images):
    fname = 'image' + str(i) + '.png'
    image.save(fname, "PNG") 