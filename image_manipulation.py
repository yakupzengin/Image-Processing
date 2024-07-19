import cv2
import matplotlib.pyplot as plt
from glob import glob

# Image Manipulation

cats_files = glob("dataset/*.jpg")
img = cv2.imread(cats_files[0])
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow('Orginal Image',img)
cv2.imshow('Grayed Image',img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()