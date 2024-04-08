import requests

def get_custom_field_id(api_key, custom_field_name):
    headers = {
        "X-Auth-Token": f"api-key {api_key}",
        "Content-Type": "application/json"
    }
    
    url = "https://api.getresponse.com/v3/custom-fields"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        custom_fields = response.json()
        for field in custom_fields:
            if field['name'] == custom_field_name:
                return field['customFieldId']
        
        print(f"Custom field '{custom_field_name}' not found.")
    else:
        print("Error retrieving custom fields from GetResponse:")
        print(response.text)

# Example usage
api_key = 'dgu0ey72kqsfsfcnzn5zt71yqbw2cbyc'
custom_field_name = 'contact_message'

custom_field_id = get_custom_field_id(api_key, custom_field_name)
if custom_field_id:
    print(f"Custom field ID: {custom_field_id}")
