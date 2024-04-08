import requests

def get_campaign_id(api_key, campaign_name):
    url = "https://api.getresponse.com/v3/campaigns"
    headers = {
        "X-Auth-Token": f"api-key {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        campaigns = response.json()
        for campaign in campaigns:
            if campaign["name"] == campaign_name:
                return campaign["campaignId"]
    else:
        print("Error retrieving campaign ID:")
        print(response.text)

# Example usage
api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
campaign_name = 'EDK NewsLetter'
campaign_id = get_campaign_id(api_key, campaign_name)

if campaign_id:
    print(f"Campaign ID for '{campaign_name}': {campaign_id}")
else:
    print("Campaign not found.")
