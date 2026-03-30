import cv2
import numpy as np
#houghcircles
image = cv2.imread("img.jpg",1)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

grayblur = cv2.blur(gray,(3,3))

detected_circle = cv2.HoughCircles(grayblur,cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2 = 30,minRadius = 1,maxRadius =40)
print(detected_circle)

if detected_circle is not None:
    detected_circle = np.uint16(np.around(detected_circle))
    print(detected_circle)
    for i in detected_circle[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(image,(x,y),r,(0,0,255),2)
        cv2.circle(image,(x,y),1,(255,0,0),3)
    cv2.imshow("detect circle",image)
    cv2.waitKey(0)
cv2.destroyAllWindows()

"""Detection Method: OpenCV has an advanced implementation, HOUGH_GRADIENT, 
which uses gradient of the edges instead of filling up the entire 3D accumulator matrix, thereby speeding up the process.
dp: This is the ratio of the resolution of original image to the accumulator matrix.
minDist: This parameter controls the minimum distance between detected circles.
Param1: Canny edge detection requires two parameters — minVal and maxVal. Param1 is the higher threshold of the two. The second one is set as Param1/2.
Param2: This is the accumulator threshold for the candidate detected circles. By increasing this threshold value, we can ensure that only the best circles, corresponding to larger accumulator values, are returned.
minRadius: Minimum circle radius.
maxRadius: Maximum circle radius."""

