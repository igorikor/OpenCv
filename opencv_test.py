import numpy as np
import cv2

vid = cv2.VideoCapture(0)

img = cv2.imread('photo1.jpg',1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while vid.isOpened():
	ref, frame = vid.read()

	cv2.imshow('photo',img)

	cv2.imshow('frame',frame)

	print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

	if cv2.waitKey(1) == ord('p'):
		cv2.imwrite('photo1.jpg',frame)

	if cv2.waitKey(1) == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
