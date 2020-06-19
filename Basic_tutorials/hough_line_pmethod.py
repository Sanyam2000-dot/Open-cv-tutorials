import cv2
import numpy as np
img=cv2.imread("sudoku.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,35,100,apertureSize=3)
cv2.imshow("edges",edge)
lines=cv2.HoughLinesP(edge,1,np.pi/180,200,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x,y=line[0]
    cv2.line(img,(x1,y1),(x,y),(0,255,0),2)
cv2.imshow("houghlines",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
