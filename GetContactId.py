

import requests
import json

# Set your GetResponse API key and campaign ID
api_key = "dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc"
campaign_id = "5f6aN"
email_to_match = "harish.s@mayutech"

# Set the API endpoint URL
url = f"https://api.getresponse.com/v3/campaigns/{campaign_id}/contacts"

# Set the headers with the API key
headers = {
    "X-Auth-Token": f"api-key {api_key}",
    "Content-Type": "application/json"
}

# Send a GET request to retrieve contacts from the campaign
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
   
    
    # Extract the contacts from the response
    contacts = data["contacts"]
    
    # Search for the contact with the specified email
    matched_contact_id = None
    for contact in contacts:
        # Extract the email of each contact
        email = contact["email"]
        
        # Check if the email matches the desired email
        if email == email_to_match:
            matched_contact_id = contact["contactId"]
            break
    
    # Process the matched contact ID
    if matched_contact_id:
        print(f"Contact ID: {matched_contact_id}")
    else:
        print("No contact found with the specified email.")
else:
    print(f"Error: {response.status_code} - {response.text}")

