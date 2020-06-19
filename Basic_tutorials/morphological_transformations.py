import numpy as np
import cv2
from matplotlib import pyplot as plt
img= cv2.imread("smarties.png",0)
_,mask=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
kernal=np.ones((5,5),np.uint8)
dilation=cv2.dilate(mask,kernal)
titles=["image","mask","dilation"]
images=[img,mask,dilation]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
plt.show()
