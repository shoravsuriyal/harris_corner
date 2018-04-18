import cv2
import numpy as np

cam=cv2.VideoCapture(0)


while True:

    ret,frame=cam.read()
    if ret==True:
        cv2.imwrite("1.png",frame)
        img = cv2.imread('1.png')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,5,3,0.04)
    

        dst = cv2.dilate(dst,None)

        img[dst>0.01*dst.max()]=[0,0,255]

        cv2.imshow('Workbench',img)
    if not ret:
        break
    
    if cv2.waitKey(1) & 0xff == 27:
        cam.release()
        cv2.destroyAllWindows()
