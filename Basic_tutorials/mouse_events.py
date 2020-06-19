import cv2
import numpy as np
def click_event(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN:
         print('x' + ',' + 'y')
         font=cv2.FONT_HERSHEY_COMPLEX
         strXY=str(x)+' '+ str(y)
         cv2.putText(img, strXY, (x, y), font, .5, (255,0,0), 2 )
         cv2.imshow("image",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + ' ' + str(green)+' '+str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 0), 2)
        cv2.imshow("image", img)


#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("messi5.jpg", 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
