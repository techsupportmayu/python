import base64
import os
from flask import Flask, send_from_directory
import requests

app = Flask(__name__)

# Function to decode Base64 data and save it as a temporary file
def save_base64_image(base64_data):
    image_data = base64.b64decode(base64_data)
    with open("temp_image.jpg", "wb") as file:
        file.write(image_data)

# Route to upload Base64 image data and get the image URL
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.form:
        base64_data = request.form['image']
        save_base64_image(base64_data)
        # Replace with your actual server domain and path
        image_url = f"https://example.com/images/temp_image.jpg"
        return image_url
    else:
        return "No image data provided."

if __name__ == '__main__':
    app.run(debug=True)
