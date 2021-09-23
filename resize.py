#!/usr/bin/python
from PIL import Image
import os, sys
path = "images/"
dirs = os.listdir( path )
def resize():
    for item in dirs:
        for f in os.listdir(path+item):
            fpath = os.path.join(path+item, f)
            if os.path.isfile(fpath):

                im = Image.open(fpath)
                print("open",im)
                f, e = os.path.splitext(fpath)
                imResize = im.resize((256,256), Image.ANTIALIAS)
                print("resize", imResize)
                imResize.save(fpath + ' resized.jpg', 'JPEG', quality=90)
                os.unlink(fpath)

#resize()
#./resize.py
#chmod 755 resize.py
