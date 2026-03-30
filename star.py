import cv2
image = cv2.imread("white2.jpg") 

cv2.line(image,(70,300),(200,50),(255,0,0),2)
cv2.line(image,(300,300),(200,50),(255,0,0),2)
cv2.line(image,(300,300),(80,120),(255,0,0),2)
cv2.line(image,(70,300),(310,120),(255,0,0),2)
cv2.line(image,(80,120),(310,120),(255,0,0),2)


cv2.imshow("output",image)
cv2.waitKey(0)
cv2.destroyAllWindows()