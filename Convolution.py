import matplotlib.pyplot as plt
import skimage.measure as msr
from PIL import Image
import numpy as np
import ast

#---Open-Images------------------------------------------------------
imageFile = Image.open("Images/Trump.jpg")
imageFile = imageFile.convert('L')
imageArray = np.array(imageFile)
xImg, yImg = len(imageArray), len(imageArray[0])

filterFile = Image.open("Filters/Line4.jpg")
filterFile = filterFile.convert('L')
filterArray = np.array(filterFile)
xFilter, yFilter = len(filterArray[0]), len(filterArray)

xNew, yNew = int((xImg-xFilter)/1+1), int((yImg-yFilter)/1+1)

print("[Origin] Height: %d, Width: %d" %(xImg, yImg))
print("[Filter] Height: %d, Width: %d" %(xFilter, yFilter))
print("[Result] Height: %d, Width: %d" %(xNew, yNew))
#---Open-Images--END-------------------------------------------------

#===Preprocessing====================================================
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ConvolutionList = []
for x in range(xNew):
    for y in range(yNew):
        ConvolutionList.append(imageArray[x:x+xFilter, y:y+yFilter] * filterArray)
#----------------------------------------------------------

#++Convert[144[x[y[1]]]] to [144[float(x)]]++++++++++++++++
for i in range(xNew*yNew):
    ConvolutionList[i] = int(np.mean(ConvolutionList[i]))
#----------------------------------------------------------

#++Convert[144[float(x)]] to [12[12[float(x)]]]++++++++++++
Buffer = []
for i in range(0, xNew*yNew, yNew):
    Buffer.append(ConvolutionList[i:i+yNew])
#----------------------------------------------------------

#++Put values frim list to ndarray+++++++++++++++++++++++++
Img = np.empty((xNew,yNew))
for x in range(xNew):
    for y in range(yNew):
        Img[x][y] = int(Buffer[x][y])
#----------------------------------------------------------
#====================================================================

Img = Image.fromarray(Img)
Img = Img.convert('L')
Img.save("Result.jpg")
