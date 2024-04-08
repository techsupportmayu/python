import requests
import json

def create_campaign(api_key, campaign_name):
    url = 'https://api.getresponse.com/v3/campaigns'
    headers = {
        'X-Auth-Token': 'api-key {}'.format(api_key),
        'Content-Type': 'application/json'
    }

    data = {
        'name': campaign_name
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print('Campaign "{}" created successfully.'.format(campaign_name))
    else:
        print('Failed to create campaign. Status code: {}'.format(response.status_code))

# Replace 'YOUR_API_KEY' with your GetResponse API key
api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
campaign_name = 'Contact Us'

create_campaign(api_key, campaign_name)
