import numpy as np
import cv2

vid = cv2.VideoCapture(0)

while vid.isOpened():
	ref, frame = vid.read()

	cv2.imshow('frame',frame)

	print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

	if cv2.waitKey(1) == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
