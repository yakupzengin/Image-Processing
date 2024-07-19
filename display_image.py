from matplotlib import pyplot as plt

def display_image_with_matplolib(image,title):

    fig, ax = plt.subplots(figsize=(60, 30))
    ax.imshow(image)
    ax.axis('off')
    ax.set_title(title,fontsize=100)
    plt.show()
