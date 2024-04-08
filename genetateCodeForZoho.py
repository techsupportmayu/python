def generate_auth_url(client_id, redirect_uri, scope, state, response_type="code", access_type="offline"):
    base_url = "https://accounts.zoho.com/oauth/v2/auth"
    auth_params = {
        "scope": scope,
        "client_id": client_id,
        "state": state,
        "response_type": response_type,
        "redirect_uri": redirect_uri,
        "access_type": access_type
    }
    auth_url = base_url + "?" + "&".join([f"{k}={v}" for k, v in auth_params.items()])
    return auth_url

# Example parameters
client_id = "1000.V9OB7606ZKJWSEZ10B1J5P218I6UYN"
redirect_uri = "https://www.mayutech.com/contact-us"
scope = "ZohoInventory.invoices.CREATE,ZohoInventory.invoices.READ,ZohoInventory.invoices.UPDATE,ZohoInventory.invoices.DELETE"
state = "testing"

# Generate the authorization URL
auth_url = generate_auth_url(client_id, redirect_uri, scope, state)
print("Authorization URL:", auth_url)
