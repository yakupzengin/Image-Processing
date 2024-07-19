import pandas as pd
from glob import glob
import cv2
import matplotlib.pylab as plt

# Image Channels
# Dısplay RGB Channels of our image

cats_files = glob("dataset/*.jpg")
img_mp1 = plt.imread(cats_files[1])
img_cv2 = cv2.imread(cats_files[1])

fig , axs = plt.subplots(1,3,figsize=(60,30))
axs[0].imshow(img_mp1[:,:,0], cmap="Reds")
axs[1].imshow(img_mp1[:,:,1], cmap="Greens")
axs[2].imshow(img_mp1[:,:,2], cmap="Blues")

axs[0].axis("off")
axs[1].axis("off")
axs[2].axis("off")
axs[0].set_title("Red Channel",fontsize =100)
axs[1].set_title("Green Channel",fontsize =100)
axs[2].set_title("Blue Channel",fontsize =100)

plt.show()