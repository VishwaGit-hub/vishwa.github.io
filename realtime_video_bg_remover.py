import cv2 as cv
import numpy as np
import cvzone 
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

listimg=os.listdir('C:/Users/Vishwa/Desktop/Msc AIMl/BackgroundVideo/images')
imglist=[]
print('listimg is',listimg)
for imgpath in listimg:
    img=cv.imread(f'C:/Users/Vishwa/Desktop/Msc AIMl/BackgroundVideo/images/{imgpath}')
    img = cv.resize(img, (640, 480))
    imglist.append(img)

print('Image list is',imglist)

imgindex=0



segmentor=SelfiSegmentation()

while True:
    success,img=cap.read()
    imgOut=segmentor.removeBG(img,imglist[imgindex],cutThreshold=0.3)

    imgStacked= cvzone.stackImages([img,imgOut],2,1)
    cv.imshow('Image',imgStacked)
    

    k=cv.waitKey(1)  

    if k==ord('a'):
        imgindex = (imgindex - 1) % len(imglist)  # cycle left
    
    elif k==ord('d'):
        imgindex = (imgindex + 1) % len(imglist)    
    elif k==ord('q'):
        break
    

    

cap.release()
cv.destroyAllWindows()


