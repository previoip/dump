import os
from PIL import Image, ImageFilter, ImageOps
from numpy import asarray

dither = True
img = []
fileInput = 'sample2.png'
basewidth = 196
finalwidth = 32
class bitmapToBraille:
    def __init__(self, filename: str, dither: bool = True, treshold: float = 0.5):
        with Image.open(filename) as im:            
            if dither:
                wpercent = (finalwidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                im = im.resize((finalwidth,hsize), Image.ADAPTIVE).filter(ImageFilter.SHARPEN).filter(ImageFilter.EDGE_ENHANCE)
                            
                if im.mode == 'RGBA':
                    r,g,b,a = im.split()
                    rgb_image = Image.merge('RGB', (r,g,b))
                    inverted_image = ImageOps.invert(rgb_image)
                    r2,g2,b2 = inverted_image.split()
                    im = Image.merge('RGBA', (r2,g2,b2,a))
                else:
                    im = ImageOps.invert(im)
                
                imtemp = im.convert('1')
                
            
            else:
                wpercent = (basewidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                im = im.resize((basewidth,hsize), Image.LANCZOS)

                im.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.CONTOUR)
                imtemp = im.convert('L').point(lambda x : 0 if x > int(255 * treshold) else 255, mode = '1')

                wpercent = (finalwidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                imtemp = imtemp.resize((finalwidth,hsize), Image.ADAPTIVE).filter(ImageFilter.SHARPEN)
            self.image = imtemp
        pass

    def export(self, filename: str = "example.png"):
        self.image.save(filename)

    def toBraille(self):

        def ceil(n):
            return int(-1 * n // 1 * -1)

        def utfconv(lst=[0,0,0,0,0,0,0,0]):
            offset = 10240
            for i in range(len(lst)):
                offset += lst[i]*pow(2, i)
            #return offset
            return chr(offset)

        def embedArray(arr, dimension = (0, 0)):
            x, y = dimension
            temparr = [[0 for i in range(x)] for j in range(y)]
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    temparr[i][j] = arr[i][j]
            return temparr

        temp = asarray(self.image)

        w, h = (2, 4)
        x, y = ( len(temp[0]), len(temp) )
        nx, ny = ((ceil(x/w)*w if x%w else x), (ceil(y/h)*h if y%h else y))

        temp = [[(1 if x else 0) for x in y] for y  in temp]
        arrconv = embedArray(temp, (nx, ny))
        returnarr = []
        
        for iy in range(0, ny, h):
            for ix in range(0, nx, w):
                returnarr.append(utfconv([
                    arrconv[iy][ix], arrconv[iy+1][ix], 
                    arrconv[iy+2][ix], arrconv[iy][ix+1], 
                    arrconv[iy+1][ix+1], arrconv[iy+2][ix+1], 
                    arrconv[iy+3][ix], arrconv[iy+3][ix+1]
                ]))
        
        returnstr = ""
        returnarr = [returnarr[n:n+int(nx/w)] for n in range(0, len(returnarr), int(nx/w))]
        for val in returnarr:
            returnstr += "".join(val) +"\n"
        return returnstr

stringData = bitmapToBraille(fileInput, False, 0.1)
# stringData.image.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0))

braille = stringData.toBraille()

with open(f"braille-02.txt", 'w', encoding="utf-8") as filehandle:
    filehandle.write(braille)
