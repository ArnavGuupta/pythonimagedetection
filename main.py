import cv2
import numpy as num
img = cv2.imread(r"C:\Users\Arnav Gupta\Downloads\.ipynb_checkpoints\img1.jpg.jpg")
re_img = cv2.resize(img,(400,300))
cv2.imshow("Tech",re_img)
cv2.waitKey(1000)

