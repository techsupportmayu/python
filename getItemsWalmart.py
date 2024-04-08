import time
import base64
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

class Walmart:

    def __init__(self, config):
        self.host = config['host']
        self.consumer_id = config['consumer_id']
        self.private_key_content = config['private_key_content']
        self.sec_key_version = config['sec_key_version']
        self.client = requests.Session()

    def lookup_product(self, publisher_id='', ids='', upc='', format='json'):
        self.load_options()

        url_params = {
            'format': format,
        }

        if publisher_id:
            url_params['publisher_id'] = publisher_id

        if ids:
            url_params['ids'] = ids

        if upc:
            url_params['upc'] = upc

        url = f"{self.host}/product/v2/items"
        response = self.client.get(url, params=url_params, headers=self.options['headers'])

        if response.status_code == 200:
            return response.json()
        else:
            return {
                'error': f"API Call Failed with Status Code: {response.status_code}",
                'response_content': response.text
            }

    def load_options(self):
        timestamp = str(int(time.time() * 1000))
        self.options = {
            'debug': False,
            'headers': {
                'WM_SEC.KEY_VERSION': self.sec_key_version,
                'WM_CONSUMER.ID': self.consumer_id,
                'WM_CONSUMER.INTIMESTAMP': timestamp,
                'WM_SEC.AUTH_SIGNATURE': self.get_signature(timestamp)
            }
        }

    def get_signature(self, timestamp):
        message = f"{self.consumer_id}\n{timestamp}\n{self.sec_key_version}\n"

        private_key = serialization.load_pem_private_key(
            self.private_key_content.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

        signature = private_key.sign(
            message.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return base64.b64encode(signature).decode('utf-8')

# Configuration
config = {
    'host': 'https://developer.api.walmart.com/api-proxy/service/affil',
    'consumer_id': 'YOUR_CONSUMER_ID',
    'private_key_content': '''YOUR_PRIVATE_KEY_CONTENT''',
    'sec_key_version': '4',  # Adjust as needed
}

walmart = Walmart(config)
response = walmart.lookup_product(publisher_id='YOUR_PUBLISHER_ID')

print(response)
