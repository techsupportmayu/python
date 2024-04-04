from twilio.rest import Client

# Twilio credentials
account_sid = 'ACb92a9acd8eb83a9a40c9162f433da1b9'
auth_token = '6c9ab3f81148b7a63c438ca43e5b7f87'

# Twilio phone number and recipient's phone number
twilio_phone_number = '06280613525'
recipient_phone_number = '+91 6280613525'

# Generate a random code for authentication
import random
code = ''.join(random.choices('0123456789', k=6))

# Create Twilio client
client = Client(account_sid, auth_token)

# Send the code via SMS
message = client.messages.create(
                              body=f'Your verification code is: {code}',
                              from_=twilio_phone_number,
                              to=recipient_phone_number
                          )

print("SMS sent successfully!")
