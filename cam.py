
import cv2.cv as cv
import time

cv.NamedWindow('Webcam')
capture = cv.CaptureFromCAM(0)
t = Timer(30.0,camloop)
  
def cammy():
        frame = cv.QueryFrame(capture)
        cv.ShowImage('Webcam', frame)
        x=1
        while True:
                def Camloop():
                        c = cv.WaitKey(10)
                        cv.SaveImage('image %d.jpg' % (x), frame)
                        x+=1
                        t.start()
cv.DestroyAllWindows()

