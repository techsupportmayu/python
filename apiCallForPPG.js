import requests
import json

url = "https://api.precisionproco.co.uk/order"

payload = json.dumps({
  "requestType": {
    "type": "Order"
  },
  "order": {
    "source": "paperjournals",
    "sourceOrderId": "10189",
    "currency": "GBP",
    "customerOrderId": "123456789",
    "dueDate": "0001-01-01T00:00:00",
    "requiresFileProcess": False,
    "destination": "precision",
    "extraData": {
      "redo": False,
      "dueDate": "2022-06-16T19:00:00.000Z",
      "brand": "Brand"
    },
    "tags": None,
    "transactionId": "c631a5d0-e73b-45cb-96ae-34a8a4af3ea3",
    "timestamp": "2022-06-15T13:21:09.623Z"
  },
  "shipments": [
    {
      "shipmentIndex": 0,
      "shippingAddress": {
        "name": "CustomerName",
        "companyName": "CompanyName",
        "address1": "Address Line1",
        "address2": None,
        "address3": None,
        "town": "London",
        "postcode": "RM9 6FB",
        "state": None,
        "isoCountry": "GB",
        "country": None,
        "email": "harish.s@mayutech.com",
        "phone": "0741111111"
      },
      "returnAddress": {
        "name": "Sender",
        "companyName": "Sender Company",
        "address1": "Address Line1",
        "address2": "Address Line2",
        "address3": None,
        "town": "London",
        "postcode": "RM9 6FB",
        "state": None,
        "isoCountry": "GB",
        "country": "United Kingdom",
        "email": "email@email.com",
        "phone": "02011111111"
      },
      "shippingAlias": "rm48tracked",
      "shippingCost": {
        "value": "3.99",
        "currency": "GBP"
      },
      "attachments": None
    }
  ],
  "items": [
    {
      "shipmentIndex": 0,
      "itemId": "179103434_210542511",
      "barcode": "210542511-1095720601",
      "extraData": {
        "productName": "wrappingpaper001",
        "commodityCode": "4911910090",
        "tracked": "true"
      },
      "sku": "PPJ_NTB_148x210_HC_Lined",
      "quantity": 1,
      "harmonizedCode": "4911910090",
      "unitPrice": 1,
      "unitWeight": 0,
      "components": [
        {
          "componentId": "222614523_210542511",
          "barcode": None,
          "code": "WRAPPINGPAPER",
          "pages": 1,
          "fetch": True,
          "path": "https://pdf.pitchprint.com/f0552e1b74e3e0e1ba2d239c9631b53a19",
          "attributes": None
        }
      ]
    }
  ],
  "stockItems": []
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJraWQiOiJETlNcL3JKRlY2dDN3TmFPZjNZM1JRSmhJekdiZkpuSnFVWHhVWGRtMlwvUlU9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJmMWZlOWRjOS1lY2JmLTQ2M2UtYjdlNy0yODk2NDc1NjMwMDYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfOXZxVkxJRlcwIiwiY29nbml0bzp1c2VybmFtZSI6InBhcGVyam91cm5hbHByb2R1c2VyIiwib3JpZ2luX2p0aSI6ImY3ZDIxY2E3LWEzYzMtNGI3OC05ZWI4LWU5Y2JjMGQwMWFmOSIsImF1ZCI6IjRmYm80bnFhc2wxazc3bm1rN2twdDRpbnE3IiwiY3VzdG9tOnNvdXJjZUFjY291bnRJZCI6IjY0ZDRlNzI2NzBkODc1MDAwNzk5ZDQ5NyIsImV2ZW50X2lkIjoiNmUzNmJlNGEtYzJkMy00NTRjLWExNjEtNmJmOGRlZWI1NGZlIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2OTcwMTUzNTAsImV4cCI6MTY5NzAxODk1MCwiY3VzdG9tOnJvbGUiOiJhcGk6YWRtaW4iLCJpYXQiOjE2OTcwMTUzNTAsImp0aSI6IjA5YmM0ZDg1LTRmMTgtNGM0Ny1iZWI0LTNkNzczZTUzYTE3MSIsImVtYWlsIjoiYWRtaW5AbWF5dXRlY2guY29tIn0.VtekBeuvuWNlLKtYEIEfErVZPFivhVZbgXnZ0-4Z95yATa-G2CzUbxxjDgb-GlevDCl08mHhNfkwTxBHoQ6PHzPv5H3C3fVUfKlIdLGVK_sq94lTrOxGuqrSPt29KMhkB1M2Nnm9lAMJpjLRsi3pi0S4pm-uoOmHvidVY1ZhBEnvai0cdRLOSYelG7Ry2Y9eudwUF3tyAu023MHKAYI6P7svtafGazjdZYK_LBqbDToN5pCLbuypITRJL2eYxotYXIFp5L9E6XUiJBKLcPZ4tGfxAWCBbZ4JfJURFuwUUryMiCYGMV1GkMlThQFGJOE-_uSVZy3ifHasTNvK7P14ZA'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
