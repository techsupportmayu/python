import time
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_signature(private_key_content, string_to_sign):
    private_key = serialization.load_pem_private_key(
        private_key_content.encode('utf-8'),
        password=None,
        backend=default_backend()
    )

    signature = private_key.sign(
        string_to_sign.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return base64.b64encode(signature).decode('utf-8')

def canonicalize(headers_to_sign):
    parameter_names_buffer = []
    canonicalized_str_buffer = []
    for key in sorted(headers_to_sign.keys()):
        val = headers_to_sign[key]
        parameter_names_buffer.append(key.strip())
        canonicalized_str_buffer.append(val.strip())

    return ';'.join(parameter_names_buffer), '\n'.join(canonicalized_str_buffer)

def main():
    consumer_id = "b10ea6f3-068b-4df7-924b-b1d5ea88a31c"
    private_key_version = "1"
    private_key_content = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDOwPN0jE+7nXNi
/kHBSZjokPDDjsKwnARGdlZ8GPtnVgDB+C3FJeC7WvjHgwsk2NJstFJKCKO072T/
uwmqYg3sOn0tEc8vUgteFF7hOFPlO3dagjvSaK95d8vJ0KU4v9WSna1nbOCC7/x6
pneMWFs3mXSd13XORiUOyL5ewSmpBlCBZ82jmYNrb4w+3TKuxN2alcXZBt1/PC3b
bsVuvrknVH0Gnluhv617GQFz/Y4Qy9P9YiQKLyHD2l6Xmqpk9S4n/OKJnzwakCu4
j4HV2ohGoN598lKJztuEKj9Qdd0gA9P4dWRRKcKMJ9tQCGK2j8OQcOx5ZrsHsIKm
RLRoKViPAgMBAAECggEAdn4vCUTBDY2Xa8y8csJzWBZ5ZhqTihRgfuGjf0vyCa9I
j+JkmPC0c6wXmICKCnwZXSObZcK90BzDjazsRTIdOJ3sz7+9NimXSjvyhLF7o40J
Ql4RWu2UY9E8glWJ25RWGskzcGr94Q0ZblGpgk3BOYRBSZUKd0XMR0TVlgiuj6d+
JEhLheNr1VlXUEvmYsM7x9IgokqU5JTZjdmQEUCS2pdWCwgcutimJ0gdmL0k6H2e
HIFWftvU+G6uPK1LNAiGUe8CLOEUAFrz0KfcJLr2yhchEPsW0suYg0DUg4ry8ZTD
FGg6K70rs/nTV5w0ScQ1DkrF9k+ac0VGaKek022DgQKBgQD6a4Uw4OvxYDpA/ccA
QgqiVqtwKloKCelXDJfZLkpHxL9N3S5DV7zSsNFlaB4g1rhGLC3MFdqMHvTxhU0d
MWiXyLbgcd+6ty1INC7UwSKBj+1AfvC/66QB8trBVss2qe5/c9XZcjeYVXJU/NyM
suoXMvn8SwhY8PIFpXaibNSkWQKBgQDTXFf0LZxiDjnzkKxDAn/mBSuLeC5+nxQl
lGu9Hz59Fi1Az+spcdVDlvuDLTlbMeFYUAkxZzN2C2FfeLu/5s44hBjHLZdCWKba
trwVaZ8/VPNWLzvA3tGfZWhpf4glQhFDcYQ8DbvcV7bWheIy/ryHG1Nbsv4jsQAS
XT1uADjnJwKBgBGOxljl/EUBPTRfVruS5dH6B60mmweHKGAdFux4TWb4yXz5HAxG
s4uGMDhO84XT6DmrUU603YzjgsMIWJ7KXw39Wa0k7s3VmAwu9HWgUP4KjFTwUYrz
R52HXIUfw8HCamFvSrgjRPieTRTeYcxPoxAbV+GzlRM/WYjB0C6VONeJAoGAXgod
HAhbJwmbYTJCYsIu88HjIPfFABN5XEsQMKJBJFiEo+yefd8m+x6nIzMw7NFhqPBb
Vr7LF79ygI7wQi7IHD8x4xT20s8s1e0t+/z1nLEIX5U+ac75x4jQDvhuM92UXsSY
CDw4FI52TDZfcT8D1L0kto0KJAkxtfoERfgVWUsCgYB2G7bFcw5XutNow1Dsf+sQ
zMEQdW5tXVvWNrJfFJ1Oa34BORNakta2QPqshIHzzFHAtnq1AdyciI5apyN7tBSP
NQXluIJ7oockkXabg7BHKkGoY/qJUntcmGdHgeJ0De+P4S3QOYu871hzLaugm9kS
dCzlIvP2VRtLM38tlDorxw==
-----END PRIVATE KEY-----"""

    intimestamp = str(int(time.time() * 1000))

    print("consumerId:", consumer_id)
    print("intimestamp:", intimestamp)

    headers_to_sign = {
        "WM_CONSUMER.ID": consumer_id,
        "WM_CONSUMER.INTIMESTAMP": intimestamp,
        "WM_SEC.KEY_VERSION": private_key_version
    }

    parameter_names, canonicalized_str = canonicalize(headers_to_sign)

    try:
        signature = generate_signature(private_key_content, canonicalized_str)
        print("Signature:", signature)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
