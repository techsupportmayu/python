import requests

def make_catalog_api_call():
    base_url = "https://developer.api.walmart.com/api-proxy/service/affil/product/v2/paginated/items"
    
    # Set up query parameters
    params = {
        "category": "3944",  # Replace with your desired category ID
        "count": 100  # Number of items to return per page
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Process the response data here
        items = data.get("items", [])
        next_page = data.get("nextPage", None)
        
        # Print or process the retrieved items
        
        # If there's a next page, you can make another API call to fetch more items
        if next_page:
            make_next_page_api_call(next_page)
    else:
        print("API call failed with status code:", response)

def make_next_page_api_call(next_page_url):
    response = requests.get(next_page_url)
    if response.status_code == 200:
        data = response.json()
        # Process the response data for the next page

if __name__ == "__main__":
    make_catalog_api_call()
