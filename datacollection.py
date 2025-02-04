import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgsize = 300
counter = 0

folder = r"C:\Users\HP\OneDrive\Desktop\coding\New folder\data\yes"

while True:
    success , img =cap.read()
    hands , img = detector.findHands(img)
    if hands:
        hand=hands[0]
        x,y,w,h = hand['bbox']
        #imgwhite will give white bg to the pictures so that machine taining becomes more efficient
        imgWhite=np.ones([imgsize,imgsize,3],np.uint8)*255

        imgCrop=img[y-offset : y+h+offset,x-offset:x+w+offset]
        imgCropShape = imgCrop.shape

        aspectratio = h/w

        if aspectratio>1:
            k=imgsize/h
            wCal =  math.ceil(k*w)
            imgResize=cv2.resize(imgCrop,(wCal,imgsize))
            imgResizeShape=imgResize.shape
            wGap = math.ceil((imgsize-wCal)/2)
            imgWhite[: ,wGap : wCal+wGap]=imgResize

        else:
            k=imgsize/w
            hCal =  math.ceil(k*h)
            imgResize=cv2.resize(imgCrop,(imgsize,hCal))
            imgResizeShape=imgResize.shape
            hGap = math.ceil((imgsize-hCal)/2)
            imgWhite[hGap : hCal+hGap,:]=imgResize

        cv2.imshow('ImageCrop',imgCrop)
        cv2.imshow('ImageCrop', imgWhite)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key == ord('s') :
        counter +=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg' , imgWhite) 
        print(counter)
