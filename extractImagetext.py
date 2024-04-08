# import pytesseract
# from PIL import Image

# image_path = '/home/harish/Downloads/screenshot (4).png'

# # Open the image using PIL
# image = Image.open(image_path)

# # Perform OCR using Tesseract
# text = pytesseract.image_to_string(image)

# # Print the extracted text
# print(text)


import requests
from PIL import Image
import io
import pytesseract

# URL of the image
image_url = 'https://www.opentext.com/assets/images/OT_ShareImage_Facebook.png'

# Download the image from the URL
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))

# Perform OCR using Tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)


