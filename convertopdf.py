import requests

# Set your API key and URL
api_key = 'anil.k@mayutech.com_6cd8902b5c03535e3fdf71e3732e9b6e8271a7ddf86570558b4dfafaefe3038141cd616f'
url_to_convert = 'https://www.onairtrip.com/new-one-day-tours'

# Set the endpoint URL
endpoint = 'https://api.pdf.co/v1/pdf/convert/from/url'

# Set request headers
headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json'
}

# Set request payload
payload = {
    'url': url_to_convert
}

# Make the POST request
response = requests.post(endpoint, json=payload, headers=headers)

# Get the response JSON
result = response.json()

print(result)  # Print the response JSON for debugging

# Retrieve the download URL of the generated PDF
# Modify this line based on the actual key in the response JSON
pdf_url = result['url']

# Download the PDF file
response = requests.get(pdf_url)

# Save the PDF file to disk
with open('converted_file.pdf', 'wb') as file:
    file.write(response.content)

print('PDF conversion complete.')
