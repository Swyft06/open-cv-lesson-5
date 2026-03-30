#simple blob detecter
import cv2
import numpy as np

image = cv2.imread("img.jpg")

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.filterByCircularity = True
params.filterByConvexity = True
params.filterByInertia = True
params.minArea = 100
params.minCircularity = 0.8
params.minConvexity = 0.9
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
print(keypoints)

number_of_blobs = len(keypoints)
print("number of blob =", number_of_blobs)

blank = np.zeros((1,1))
#drawKeypoints(input_image, key_points, output_image, colour, flag)
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
text = "number of blob ="+ str(number_of_blobs)

cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
cv2.imshow("output",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()