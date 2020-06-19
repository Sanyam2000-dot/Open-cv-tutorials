import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("tracker")
cv2.createTrackbar("LH","tracker",0,255,nothing)
cv2.createTrackbar("LS","tracker",0,255,nothing)
cv2.createTrackbar("LV","tracker",0,255,nothing)
cv2.createTrackbar("UH","tracker",255,255,nothing)
cv2.createTrackbar("US","tracker",255,255,nothing)
cv2.createTrackbar("UV","tracker",255,255,nothing)
while(1):
    frame=cv2.imread("smarties.png")
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("LH","tracker")
    ls = cv2.getTrackbarPos("LS", "tracker")
    lv = cv2.getTrackbarPos("LV", "tracker")
    uh = cv2.getTrackbarPos("UH", "tracker")
    us = cv2.getTrackbarPos("US", "tracker")
    uv = cv2.getTrackbarPos("UV", "tracker")

    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k=cv2.waitKey(1)
    if k==ord("q"):
        break
cv2.destroyAllWindows()

