import cv2
from glob import glob
import numpy as np

from save_image import save_image

# Sharpen Image
cats_files = glob('dataset/*.jpg')

img = cv2.imread(cats_files[0])

kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow("Sharpened Image", sharpened)

save_image(sharpened,"sharpened_image.jpg",r"C:\Users\90544\Desktop\projects\Image-Processing\output_images")
cv2.waitKey(0)
cv2.destroyAllWindows()