import requests
import json

def subscribe_to_newsletter(api_key, campaign_id, email):
    url = 'https://api.getresponse.com/v3/contacts'
    headers = {
        'X-Auth-Token': 'api-key {}'.format(api_key),
        'Content-Type': 'application/json'
    }

    data = {
        'email': email,
        'campaign': {
            'campaignId': campaign_id
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print('Subscribed email {} to the newsletter.'.format(email))
    else:
        print('Failed to subscribe email {}. Status code: {}'.format(email, response.status_code))

# Replace 'YOUR_API_KEY' with your GetResponse API key
api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
campaign_id = '5rj3V'  # Replace with the campaign ID where you want to subscribe the contact
email = 'piyushbhardwaj403@gmail.com'  # Replace with the email you want to subscribe

subscribe_to_newsletter(api_key, campaign_id, email)
