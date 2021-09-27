#SEND SMS File
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

client = TwilioRestClient(account_sid, auth_token)
#Add your message here
my_msg = ''.join(['Hello\n' for i in range(5)])

message = client.messages.create(to=my_cell,from_=my_twilio, body=my_msg)







