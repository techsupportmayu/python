import requests

# Step 1: Register your application and get Client ID and Client Secret
client_id = "1000.V9OB7606ZKJWSEZ10B1J5P218I6UYN"
client_secret = "35528fc64309b11f2527bfa87ba89de5dc1c6d71e2"

# Step 2: Generate Grant Token
authorization_url = "https://accounts.zoho.in/oauth/v2/auth"
redirect_uri = "https://www.mayutech.com/contact-us"
scope = "ZohoInventory.fullaccess.all"  # Example scope
state = "testing"
response_type = "code"

# Redirect the user to Zoho for authorization
auth_params = {
    "scope": scope,
    "client_id": client_id,
    "state": state,
    "response_type": response_type,
    "redirect_uri": redirect_uri
}
authorization_link = authorization_url + "?" + "&".join([f"{k}={v}" for k, v in auth_params.items()])
print("Authorization URL:", authorization_link)

# After user grants permission, you'll receive a code. Use that code to get access token.
code = input("Enter the code obtained after authorization: ")

# Step 3: Generate Access Token
token_url = "https://accounts.zoho.in/oauth/v2/token"
grant_type = "authorization_code"

token_params = {
    "code": code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": grant_type
}

# Make a POST request to get access token
response = requests.post(token_url, data=token_params)
token_data = response.json()

# Step 4: Use the access token to call Zoho Inventory API
if 'access_token' in token_data:
    access_token = token_data['access_token']
    print("Access Token:", access_token)
    # Now you can make requests to Zoho Inventory API using this access token
else:
    print("Failed to get access token. Error:", token_data.get('error', 'Unknown error'))
