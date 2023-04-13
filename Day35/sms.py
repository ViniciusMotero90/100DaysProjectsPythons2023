from twilio.rest import Client

account_sid = "AC297b4024b9aac5c71c62188e1822f7ab"
auth_token = '6cbe3c16ec7fd6596ae2abdbc2e12859'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Isso e um teste',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+15005550006'
                          )