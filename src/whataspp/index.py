'''
https://zenvia.github.io/zenvia-openapi-spec/v1/#tag/WhatsApp/paths/~1channels~1whatsapp~1messages/post

Format request to send SMS -> POST
{  
  uri: 'https://api.zenvia.com/v1/channels/whatsapp/messages',
  headers: {
    'X-API-TOKEN': 'YOUR_API_TOKEN'
  },
  body: {
    from: 'sender-identifier',
    to: 'recipient-identifier',
    contents: [{
      type: 'text',
      text: 'Some text message'
    }]
  },
  json: true

To receive is by callback in webhook, we need make a POST route to the callback
}
'''

import json
import requests

from DI import ENV

url = 'https://api.zenvia.com/v1/channels/whatsapp/messages'
body = {
  'from': ENV.SENDER_ID,
  'to': ENV.RECIPIENT_TEST,
  'contents': [{
    'type': 'text',
    'text': 'Hey Bro!!'
  }]
}
headers = {
  'content-type': 'application/json',
  'X-API-TOKEN': ENV.WHATSAPP_API
}

r = requests.post(url, data=json.dumps(body), headers=headers)

print(r)