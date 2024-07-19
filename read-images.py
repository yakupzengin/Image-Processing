import pandas as pd
from glob import glob
import cv2
import matplotlib.pylab as plt

cats_files = glob("dataset/*.jpg")

# Read image using matplotlib (image is read as RGB)
img_mp1 = plt.imread(cats_files[1]) # np.array

# Read image using OpenCV (image is read as BGR)
img_cv2 = cv2.imread(cats_files[1]) # np.array

# Check if the shape of both images is the same
print(img_mp1.shape == img_cv2.shape) # True

# Matplotlib automatically converts images to RGB when displaying.
# OpenCV, however, uses BGR format. To correctly display the OpenCV image with RGB colors,
# we need to convert it from BGR to RGB.
cv2.imshow("changed to RGB", cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))

# Display the images
cv2.imshow("Matplotlib Image", img_mp1)  # Image read and displayed as RGB
cv2.imshow("OpenCV Image", img_cv2)      # Image read as BGR, showing original colors

cv2.waitKey(0)
cv2.destroyAllWindows()
