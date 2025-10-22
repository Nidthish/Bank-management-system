from twilio.rest import Client
import sys
mobile_no=sys.argv[1]
msg=sys.argv[2]
number="+91"+mobile_no
sid='sdi number'
api='api key'
ct=Client(sid,api)
ct.messages.create(body=msg,from_='dummy number',to=number)

