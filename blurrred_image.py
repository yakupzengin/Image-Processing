import cv2
from glob import glob
import numpy as np

# Blurring the Image
cats_files = glob("dataset/*.jpg")
img = cv2.imread(cats_files[0])

kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred_image= cv2.filter2D(img,-1,kernel_3x3)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()