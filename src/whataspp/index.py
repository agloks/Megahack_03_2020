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

def response_to(text, number):
  '''
  :param text: The text to response to the client
  :type text: string

  :param number: The client's number with the following format : 5511962049178
  :type number: string

  '''
  url = 'https://api.zenvia.com/v1/channels/whatsapp/messages'
  body = {
    'from': ENV.SENDER_ID,
    'to': number,
    'contents': [{
      'type': 'text',
      'text': text
    }]
  }
  headers = {
    'content-type': 'application/json',
    'X-API-TOKEN': ENV.WHATSAPP_API
  }

  result = requests.post(url, data=json.dumps(body), headers=headers)

  return result.json()

if __name__ == '__main__':

  text_to_send = "Incrivel"

  response_to_test = response_to(text_to_send, "5511985063850")

  print(response_to_test)