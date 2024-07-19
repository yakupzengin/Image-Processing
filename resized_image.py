import cv2
from glob import glob

cats_files = glob("dataset/*.jpg")
img = cv2.imread(cats_files[0])
print("original : ",img.shape)

img_resized = cv2.resize(img,None, fx=1.5,fy=1.5)
print("resized : ",img_resized.shape)
cv2.imshow("Resized Image",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Different way

img_resized = cv2.resize(img,(100,100))
cv2.imshow("Resized Image",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

