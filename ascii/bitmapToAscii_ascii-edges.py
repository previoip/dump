from typing import final
from PIL import Image, ImageFilter, ImageOps
from numpy import asarray

img = []
filename = 'k.png'
basewidth = 128
finalwidth = 128

with Image.open(filename) as im:
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ADAPTIVE)

    im_countour = im.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.CONTOUR)
    im_bw = ImageOps.colorize(im_countour.convert('L'), black="black", white="white", mid="white")
    
    wpercent = (finalwidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im_bw.resize((finalwidth,hsize), Image.ADAPTIVE).filter(ImageFilter.SHARPEN)


def invert(img: Image):
    if img.mode == 'RGBA':
        r,g,b,a = img.split()
        rgb_image = Image.merge('RGB', (r,g,b))
        inverted_image = ImageOps.invert(rgb_image)
        r2,g2,b2 = inverted_image.split()
        img = Image.merge('RGBA', (r2,g2,b2,a))
    else:
        img = ImageOps.invert(img)
    return img

im.show()

        
