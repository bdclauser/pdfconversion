from PIL import Image, ImageOps
import os
import sys

path = '/Users/brianclauser/pdfconversion/resized'


def newsize():
    os.makedirs('resized', exist_ok=True)
    for filename in os.listdir('.'):
        if not (filename.endswith('.png') or filename.endswith('jpg') or filename.endswith('jpeg')):
            continue  # skip non-image files
        im = Image.open(filename)
        print('Resizing %s...' % (filename))
        imResize = im.resize((800, 600), Image.ANTIALIAS)
        imResize.save(os.path.join(path, filename.replace("png", "jpg")))

    return newsize()