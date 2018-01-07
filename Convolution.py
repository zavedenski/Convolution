import matplotlib.pyplot as plt
import skimage.measure as msr
from PIL import Image
import numpy as np
import ast

#---Open-Origin-Image------------------------------------------------
imageFile = Image.open("Origin.jpg")
imageFile = imageFile.convert('L')
imageArray = np.array(imageFile)
imageArrayList = imageArray.tolist()
#---Open-Origin-Image--END-------------------------------------------

#---Open-Filter-Image------------------------------------------------
filterFile = Image.open("Filters/10x10.jpg")
filterFile = filterFile.convert('L')
filterArray = np.array(filterFile)
filterArrayList = filterArray.tolist()
#---Open-Filter-Image--END-------------------------------------------

#==RGB====
#print("[originImage] Colls[y]: %d, Rows[x]: %d, Layouts[z]: %d" %(len(imageArray), len(imageArray[0]), len(imageArray[0,0])))
#print("[filterImage] Colls[y]: %d, Rows[x]: %d, Layouts[z]: %d" %(len(filterArray), len(filterArray[0]), len(filterArray[0,0])))

print("[originImage] Colls[y]: %d, Rows[x]: %d" %(len(imageArray), len(imageArray[0])))
print("[filterImage] Colls[y]: %d, Rows[x]: %d" %(len(filterArray), len(filterArray[0])))

newImage = []

xLen, yLen = len(imageArray[0]), len(imageArray)
print("xLen: %d, yLen: %d" %(xLen, yLen))
xAsix, yAsix = 0, 0

while True: #Rows
    while True: #Colls
        if yAsix <= yLen-20:
            newImage.append(imageArray[xAsix:xAsix+20, yAsix:yAsix+20])
            yAsix += 1
        else:
            yAsix = 0;
            break

    if xAsix < xLen-20:
        xAsix += 1
    else:
        break

print("NewImage[0]: ", newImage[0])
print("np.mean(newImage[0]:) ", np.mean(newImage[0]))
print("NewImageLen: ", len(newImage))

for i in range(len(newImage)):
    newImage[i] = np.mean(newImage[i])


xero = np.empty((281,281))             #f(300-20)/1+1

dead = []
o = 0
while True:
    if o < 78961:
        dead.append(newImage[o:o+281])
        o += 281
    else:
        break

#print(dead[0])
print(len(dead[0]))



x, y = 0, 0
while True:
    while True:
        if y < 281:
            xero[x, y] = np.average(dead[x][y])
            y += 1
        else:
            y = 0;  break
    if x < 281:
        x +=1
    else:   break
