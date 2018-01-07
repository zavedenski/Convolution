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
#===L=====
print("[originImage] Colls[y]: %d, Rows[x]: %d" %(len(imageArray), len(imageArray[0])))
print("[filterImage] Colls[y]: %d, Rows[x]: %d" %(len(filterArray), len(filterArray[0])))

newImage = []
xLen, yLen = len(imageArray[0]), len(imageArray)
xFilter, yFilter = len(filterArray[0]), len(filterArray)
xAsix, yAsix = 0, 0

while True: #Rows
    while True: #Colls
        if yAsix <= yLen-yFilter:
            newImage.append(imageArray[xAsix:xAsix+xFilter, yAsix:yAsix+yFilter] * filterArray)
            yAsix += 1
        else:
            yAsix = 0;  break
    if xAsix < xLen-xFilter:
        xAsix += 1
    else:   break

print("NewImage[0]: ", newImage[0])
print("np.mean(newImage[0]:) ", np.mean(newImage[0]))
print("NewImageLen: ", len(newImage))

#---newImage[78961[20[20]]]------------------------------------------
for i in range(len(newImage)):
    newImage[i] = np.mean(newImage[i])  #np.max(newImage[i]) for RGB
#---newImage[78961[float64]]--End------------------------------------

#---newImage[78961[float64]]-----------------------------------------
size = int((len(imageArray) - len(filterArray))/1 + 1)
Buff = []
for i in range(0, size**2, size):
    Buff.append(newImage[i:i+size])
#---Buff[281[281[float64]]]--End-------------------------------------


xero = np.empty((size,size))             #f(300-20)/1+1
print("xero: %d, xero[0]: %d" %(len(xero), len(xero[0])))
print("Buff: %d, Buff[0]: %d" %(len(Buff), len(Buff[0])))
if len(xero) == len(Buff) and len(xero[0]) == len(Buff[0]) and type(xero[0][0]) == type(Buff[0][0]):
    print("Variables are same!")
else:
    print("Variables are difference!")

x, y = 0, 0
while True:
    while True:
        if y < size:
            xero[x][y] = int(np.mean(Buff[x][y]))
            print('[x][y] = [%d][%d] ==> %d' %(x,y, Buff[x][y]))
            y += 1
        else:
            y = 0;  break
    if x < size-1:
        x +=1
    else:   break

xeroImg = Image.fromarray(xero)
xeroImg  = xeroImg.convert('L')
xeroImg.save("Result.jpg")
