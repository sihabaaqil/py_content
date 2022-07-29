from twilio.rest import Client
import time

account_sid="ACd1f32b49c534c82fb9f19816a49f4dfa"
auth_token="d3ea16d1773698c2bcaf356dd180ff22"
client=Client(account_sid,auth_token)
from_whatapp_number = 'whatsapp:+14155238886'
# to_whatapp_number ='whatsapp:+919944380786'
# for i in range(10):
#     client.messages.create(body="Hi",from_=from_whatapp_number,to=to_whatapp_number)
#     time.sleep(1)
# to_whatapp_number ='whatsapp:+919952625956'
to_whatapp_number ='whatsapp:+919944380786'
client.messages.create(body="Hi",from_=from_whatapp_number,to=to_whatapp_number)
print("Message Sent")