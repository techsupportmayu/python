import requests

# Replace '<API_KEY>' and '<SITE_ID>' with your actual API key and site ID
API_KEY = 'IST.eyJraWQiOiJQb3pIX2FDMiIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiaWRcIjpcIjY0OTk4YTI3LTJmMjctNDkxZS05OWM5LTQxZmIxN2Q1MDkzY1wiLFwiaWRlbnRpdHlcIjp7XCJ0eXBlXCI6XCJhcHBsaWNhdGlvblwiLFwiaWRcIjpcIjUzZGI4ZThjLTc2MWEtNDFlMi05MDk0LTJiNmZlYzYxMmRkNFwifSxcInRlbmFudFwiOntcInR5cGVcIjpcImFjY291bnRcIixcImlkXCI6XCJlZDVmMDY0NC03OWIyLTQyNjYtODE3Ni1jOWQ4MDQ1MDA5ODdcIn19IiwiaWF0IjoxNzExMTA0MjMwfQ.D7TghSRoHT53C27aWuK4XfOHfYc9WYJE9_hrqWizHFCLXVd374wg8IMJ9VMnbOQ_Px9QNEc-nm6cJCEMWGTgW8XnJHXE2yuRII-ug1WtIARTq_3CNUkx1S3fphRDFrT7oUD0goEU2_7t1t90keQ5ijQ1oeUWs1SEfxGegZ1AaXZI4EdAt4CJWUH2pNfC4DhIOn-pCu0r7YTpp2ju-ykdnOarF8wsYjkUrz5ySPufIo8gCMKDFK5TWOeAiDRs-UP552FYE2lVhlzw5CXqVpTGfsDmKsbNFO_uAki7nTRMazsJ97qxATwAANzq1n_qRIMU2bNGNEcH_SLQbAmhlx--8A'
SITE_ID = '4b9a0812-2067-4180-b2ed-9113d5dc1560'

# url = 'https://www.wixapis.com/stores/v1/products/query'
url = 'https://www.wixapis.com/wix-data/v2/collections?include_referenced_collections=true&sort.field=NAME&sort.direction=ASC'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': API_KEY,
    'wix-site-id': SITE_ID
}
# payload = {
#     "query": {
#         "paging": {
#             "limit": "50"
#         }
#     }
# }


# payload = {
#     "query": {

#         "filter": {

#             "name": "Destinations"

#         }

#     }
# }

# response = requests.post(url, json=payload, headers=headers)
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful")
    data = response.json()
    print(data)  # Display the response data
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Display any error message returned by the API
