import pandas as pd
import numpy as np

from glob import glob
import cv2
import matplotlib.pylab as plt

from display_image import display_image

# Reading in Images

cats_files = glob("dataset/*.jpg")
img_mp1 = plt.imread(cats_files[1]) # np.array
img_cv2 = cv2.imread(cats_files[1]) # np.array
# print(img_mp1.shape == img_cv2.shape) # True
# Image Array ( Height, Width , Channels )
# pd.Series(img_mp1.flatten()).plot(kind="hist",
#                                   bins=50,
#                                   title="Distribution of Pixel Values")

# Display Images

# fig , axis = plt.subplots(figsize= (10,10))
# axis.imshow(img_mp1)
# axis.set_title("Original Image" , fontsize = 50)

# Image Channels
# Dısplay RGB Channels of our image
# fig , axs = plt.subplots(1,3,figsize=(60,30))
# axs[0].imshow(img_mp1[:,:,0], cmap="Reds")
# axs[1].imshow(img_mp1[:,:,1], cmap="Greens")
# axs[2].imshow(img_mp1[:,:,2], cmap="Blues")
#
# axs[0].axis("off")
# axs[1].axis("off")
# axs[2].axis("off")
# axs[0].set_title("Red Channel",fontsize =100)
# axs[1].set_title("Green Channel",fontsize =100)
# axs[2].set_title("Blue Channel",fontsize =100)
# plt.show()

"""
    Matplotlib cs cv2 Numpy Arrays
    cv2 reads in channels as BGR
    matplotlibs reads in channels as RGB
"""
# fig ,axs = plt.subplots(1,2, figsize= (60,30))
# axs[0].imshow(img_cv2)
# axs[1].imshow(img_mp1)
# axs[0].axis("off")
# axs[1].axis("off")
# axs[0].set_title("CV2 Image",fontsize =150)
# axs[1].set_title("MatplotLib Image",fontsize =150)
#
# plt.show()

# Converting from BGR to RGB
# img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
# fig , ax = plt.subplots()
# ax.imshow(img_cv2_rgb)
# ax.axis("off")
# plt.show()


# Image Manipulation
# img = plt.imread(cats_files[0])
# img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# figure , axes = plt.subplots(figsize = (8,8))
# axes.imshow(img_gray, cmap="Blues")
# axes.axis("off")
# axes.set_title("Grey Image",fontsize=30)
# plt.show()

# Resizing and Scaling
# img = plt.imread(cats_files[0])
# print("original : ",img.shape)
#
# img_resized = cv2.resize(img,None, fx=0.25,fy=0.25)
# print("resized : ",img_resized.shape)
#
# figure , axes = plt.subplots(figsize = (8,8))
# axes.imshow(img_resized)
# axes.axis("off")
# axes.set_title("Resized and Scaled Image fx:0.25, fy:0.25",fontsize=30)
# plt.show()
#
# # Different way
# img = plt.imre

# #ad(cats_files[0])
# img_resized = cv2.resize(img,(100,100))
# figure , axes = plt.subplots(figsize = (8,8))
# axes.imshow(img_resized)
# axes.axis("off")
# axes.set_title("Resize : (100,100)",fontsize=30)
# plt.show()


# Sharpening and Blurring
# # Sharpen Image
# img = plt.imread(cats_files[0])
# kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpened = cv2.filter2D(img, -1, kernel_sharpening)
# displayer = display_image(sharpened,"Sharpen Image")

# Blurring the Image
img = plt.imread(cats_files[0])
kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred_image= cv2.filter2D(img,-1,kernel_3x3)
displayer = display_image(img,"Original Image")
displayer2 = display_image(blurred_image,"Blurred Image")

# Save Image

plt.imsave("output_images/blurred_cat_files0.jpg", blurred_image)
print(cv2.imwrite("output_images/blurred_cat_files0.jpg", blurred_image))