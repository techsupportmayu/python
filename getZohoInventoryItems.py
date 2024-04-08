import requests

# Replace these variables with your Zoho Inventory organization ID and auth token
organization_id = '60027263857'
auth_token = '1000.1c11a11b8763b7ed9a4f3a7bc520e868.8f8c231545def1da5a382f66a0dad5e2'

# URL for fetching items
url = f'https://inventory.zoho.in/api/v1/items'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {auth_token}',
    'X-com-zoho-inventory-organizationid': organization_id
}

# Send GET request to fetch items
response = requests.get(url, headers=headers)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Extract items from response JSON
    items = response.json()['items']
    
    # Print item details
    for item in items:
        print(f"Item ID: {item['item_id']}")
        print(f"Item Name: {item['name']}")
        print(f"Description: {item['description']}")
        print(f"Rate: {item['rate']}")
        print("------------------------------")
else:
    print(f"Failed to fetch items. Status code: {response.status_code}")
    print(response.text)
