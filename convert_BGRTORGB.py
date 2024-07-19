"""
    The plots gave the same output for the images in BGR and RGB formats.
    However, when using cv2's imshow, the red apple turned blue when converted to RGB.
"""

import cv2
from display_image import display_image


# Read a different image file
img_cv2 = cv2.imread("dataset/red_apple.jpg")

# Check the shape and type of the image
print(f"Original image shape: {img_cv2.shape}, dtype: {img_cv2.dtype}")

# Convert from BGR to RGB
img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
print(f"Converted BGR to RGB: {img_cv2_rgb.shape}, dtype: {img_cv2_rgb.dtype}")
cv2.imshow("Original Image (BGR)", img_cv2)
cv2.imshow("Converted BGR to RGB", img_cv2_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
