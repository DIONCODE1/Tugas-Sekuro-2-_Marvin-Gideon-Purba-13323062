#Nama/NIM : Marvin Gideon Purba/13323062
#Creating bounding rectangle surrounding the object

import cv2
import numpy as np
image = cv2.imread('frame_0000.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Bounding Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#sourcecode : https://docs.opencv.org/4.x/d9/df8/tutorial_root.html





