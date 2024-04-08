import requests

def get_contacts(api_key, campaign_id):
    url = f"https://api.getresponse.com/v3/contacts"
    headers = {
        "X-Auth-Token": f"api-key {api_key}",
        "Content-Type": "application/json"
    }

    params = {
        "campaignId": campaign_id
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        contacts = response.json()
        return contacts
    else:
        print("Error retrieving contacts from GetResponse:")
        print(response.text)
        return None

# Set your GetResponse API key and campaign ID
api_key = "dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc"
campaign_id = "5rj3V"

 

# Get list of contacts
contacts = get_contacts(api_key, campaign_id)

if contacts:
    print("List of contacts:",contacts);
    for contact in contacts:
       
        print(f"Name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print("-----")
