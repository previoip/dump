import random, os, PIL, numpy
from PIL import Image
from numpy import asarray 

fileInput = 'sample.png'

strCache = ''
a= 0
b= 0
imgCache = []
styles = []

html = {
    "header": '<?xml version="1.0" encoding="utf-8"?>\n',
    "svg": ["""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox=" """,""" ">\n""","</svg>"],
    "css": ['<style type="text/css">\n','</style>\n'],
    "text": ['<text transform="translate(0 25.39)" class="fo">\n','</text>\n'],
    "defstyles": '.fo {font-family:"consolas"; font-size:31px; fill:#666}\n'
    }

dx = 17.043953
dy = 34.0
#w = 64
#h = 149

divs = 3
#colorRange = (102, 235)
colorRange = (51, 235)


#greyscale color table generator
def getGreyTable(minv, maxv, div):
    colorIter = round((maxv-minv)/div)
    x = []
    for i in range(div):
        x.insert(i, ''.join(format(minv+(colorIter*i)+j,"02x") for j in range(3)))
    x.insert(div+1, ''.join(format(maxv+j,"02x") for j in range(3)))
    return x


#program begin
def getStr(x=2):
    i = "0123456789abcdef"
    return ''.join(random.choice(i) for j in range(x))

def tspan(x, y, colorClass, string):
    return '<tspan x="'+str(x)+'" y="'+str(y)+'" class="'+colorClass+'">'+string+'</tspan>\n'        


#img conversion
img = asarray(PIL.Image.open(fileInput))

#img color treshold conversion
arrx=[]
arr=[]
for row in range(len(img[:])):
    for col in range(len(img[0][:])):
        gr = (img[row][col][0]/3)+(img[row][col][1]/3)+(img[row][col][2]/3)+1
        gr = int(round(gr/(255/divs)))
        arrx.insert(col, gr)
    arr.insert(row, arrx)
    arrx=[]
arrx.clear


a=0
for row in range(len(arr[:])):
    imgCache.insert(row, [])
    for col in range(len(arr[0][:])):
        if(arr[row][col]==arr[row][(col+1)%len(arr[0][:])]):
            a=a+1
        else:
            imgCache[row].append((a+1,arr[row][col]))
            a=0
    if(a):
        imgCache[row].append((a,arr[row][col]))
    a=0


#html init
strCache = html['header'] + html['svg'][0] + '0 0 ' + str(round(len(arr[0])*(dx*2), 1)) +' '+ str(round(len(arr)*dy, 1)) + html['svg'][1]+ html['css'][0] + html['defstyles']
for nst, vst in enumerate(getGreyTable(colorRange[0], colorRange[1], divs)):
    strCache = strCache + '.c' + str(nst) + '{fill:#' + vst + '}\n'
    styles.insert(nst,('c'+str(nst), '#'+vst))
strCache = strCache + html['css'][1] + html['text'][0]
arr.clear()

a=0
for j in range(len(imgCache[:])):
    for i in range(len(imgCache[j][:])):
        strCache = strCache + tspan(round(a, 3),round((j*dy), 3),styles[imgCache[j][i][1]][0],getStr(imgCache[j][i][0]*2))
        a = a + imgCache[j][i][0]*(dx*2)
    a=0
strCache = strCache + html['text'][1] + html['svg'][2]

print(strCache)
#print(imgCache)

with open(f"test.svg", 'w') as filehandle:
    filehandle.write(strCache)
