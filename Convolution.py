import matplotlib.pyplot as plt
from skimage import img_as_ubyte
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
filterFile = Image.open("Filters/line3.jpg")
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
            yAsix = 0;  break
    if xAsix < xLen-20:
        xAsix += 1
    else:   break

print("NewImage[0]: ", newImage[0])
print("np.mean(newImage[0]:) ", np.mean(newImage[0]))
print("NewImageLen: ", len(newImage))

#---newImage[78961[20[20]]]------------------------------------------
for i in range(len(newImage)):
    newImage[i] = np.mean(newImage[i])
#---newImage[78961[float64]]--End------------------------------------

#---newImage[78961[float64]]-----------------------------------------
Buff = []
for i in range(0, 78961, 281):
    Buff.append(newImage[i:i+281])
#---Buff[281[281[float64]]]--End-------------------------------------


xero = np.empty((281,281))             #f(300-20)/1+1
print("xero: %d, xero[0]: %d" %(len(xero), len(xero[0])))
print("Buff: %d, Buff[0]: %d" %(len(Buff), len(Buff[0])))
if len(xero) == len(Buff) and len(xero[0]) == len(Buff[0]) and type(xero[0][0]) == type(Buff[0][0]):
    print("Variables are same!")
else:
    print("Variables are difference!")

x, y = 0, 0
while True:
    while True:
        if y < 281:
            xero[x][y] = int(np.mean(Buff[x][y]))
            print('[x][y] = [%d][%d] ==> %d' %(x,y, Buff[x][y]))
            y += 1
        else:
            y = 0;  break
    if x < 281-1:
        x +=1
    else:   break

xeroImg = Image.fromarray(xero)
xeroImg  = xeroImg.convert('L')
xeroImg.save("Result.jpg")
