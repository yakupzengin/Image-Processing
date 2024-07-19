import cv2

def save_image(image, new_name, path_to_save):

    full_path = f"{path_to_save}/{new_name}"
    success = cv2.imwrite(full_path, image)
    if success:
        print(f"Image successfully saved to {full_path}")
    else:
        print(f"Failed to save image to {full_path}")
