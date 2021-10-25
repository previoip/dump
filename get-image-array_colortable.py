import numpy as np
from PIL import Image


imageFile = 'img.png'

img = PIL.Image.open(imageFile)
img_data = np.asarray(img)


print(np.shape(img_data)[0])
print(np.shape(img_data)[1])
l = np.shape(img_data)[0]
h = np.shape(img_data)[1]

mt = []
tl = []
tl_check = []
i = 0
j = 0
rch = 0
temp = []


for row in range(0, len(img_data[:])):
    for col in range(0, len(img_data[0][:])):
        r = format(img_data[row][col][0],"02x")
        g = format(img_data[row][col][1],"02x")
        b = format(img_data[row][col][2],"02x")
        a = format(img_data[row][col][3],"02x")
        img_hex = str(r)+str(g)+str(b)+str(a)
        if img_hex in tl_check:
            img_hex = format((tl_check.index(img_hex)), "02d")
        else:
            tl_check.append(img_hex)
            img_hex = format((tl_check.index(img_hex)), "02d")
            
        tl.insert(col, img_hex)
    mt.insert(row, tl)
    tl = []


tl.clear

mt_tuple = list(zip(*mt))
print(mt)
print(tl_check)



for ro in range(0, len(mt_tuple[:])):
    for cl in range(0, len(mt_tuple[0][:])):
        if(mt_tuple[ro][cl] == mt_tuple[ro][(cl+1)%len(mt_tuple[0][:])]):
            i = i+1
        else:
            temp.append(format((i+1), "02d")+str(mt_tuple[ro][cl]))
            i = 0
    temp.append(format((i), "02d")+str(mt_tuple[ro][cl]))
    i = 0



    
filename = "array-export"
i = 0
while os.path.exists(f"{filename}{i}.txt"):
    i += 1

with open(f"{filename}{i}.txt", 'w') as filehandle:
    filehandle.write(str(temp)+"\n"+str(tl_check))

            


