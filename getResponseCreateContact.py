import requests

def send_form_data_to_getresponse(form_data):
    api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
    campaign_id = "5rj3V"
    url = f"https://api.getresponse.com/v3/contacts"
    headers = {
        "X-Auth-Token": f"api-key {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": form_data["name"],
        "email": form_data["email"],
        "campaign": {
            "campaignId": campaign_id
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Form data successfully sent to GetResponse!")
    else:
        print("Error sending form data to GetResponse:")
        print(response.text)

# Example form data
form_data = {
    "name": "John Doe",
    "email": "Harish.j@gmail.com"
}

send_form_data_to_getresponse(form_data)
