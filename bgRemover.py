import cv2
import numpy as np
import requests
from io import BytesIO

def remove_background_from_url(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    image = np.array(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Create a mask with white background
    mask = np.zeros(image.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define a rectangle region to mark the foreground (the object you want to keep)
    rectangle = (50, 50, image.shape[1] - 50, image.shape[0] - 50)  # (x, y, width, height)

    # Run the GrabCut algorithm to segment the foreground from the background
    cv2.grabCut(image, mask, rectangle, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where all foreground and probable foreground pixels are set to 1, and the rest to 0
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Multiply the original image with the mask to obtain the foreground
    result_image = image * mask2[:, :, np.newaxis]

    return result_image

if __name__ == "__main__":
    input_image_url = "https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg"  # Replace with the actual image URL
    output_image_path = "/home/harish/Downloads/image.png"

    # Call the function to remove the background
    result_image = remove_background_from_url(input_image_url)

    # Save the output image
    cv2.imwrite(output_image_path, result_image)

    print("Background removed and the result is saved to", output_image_path)
