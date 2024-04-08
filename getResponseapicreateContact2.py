import requests

def send_form_data_to_getresponse(form_data):
    api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
    campaign_id = "5rj3V"
    custom_field_id = "pCedbo"  # Replace with your custom field ID
    url = f"https://api.getresponse.com/v3/contacts"
    headers = {
        "X-Auth-Token": f"api-key {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": form_data["name"],
        "email": form_data["email"],
        "phone": form_data["phone"],
        "contact_message": form_data["message"],
        "campaign": {
            "campaignId": campaign_id
        },
        "customFieldValues": [
            {
                "customFieldId": custom_field_id,
                "value": ["hello"]  # Replace with the actual value
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Form data successfully sent to GetResponse!")
    else:
        print("Error sending form data to GetResponse:")
        print(response.text)

# Example form data
form_data = {
    "name": "rishi test",
    "email": "rishi.test@gmail.com",
    "phone": "5398405",
    "message": "Hello, GetResponse!"
}

send_form_data_to_getresponse(form_data)
