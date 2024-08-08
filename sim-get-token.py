headers = {
    'Content-Type': 'application/json',
    "Connection" : "Keep-Alive",
    # "Content-Length" : "1637",
    # "Content-Type" : "application/json",
    "Host" : "chatgpt-au.vulcanlabs.co",
    "User-Agent" : "Chat Smith Android, Version 486",
    "X-Vulcan-Application-ID" : "com.smartwidgetlabs.chatgpt",
    "X-Vulcan-Request-ID" : "9149487891706841083945"
}

import json

payload = {
  "device_id": "6429673160506935",
  "order_id": "",
  "product_id": "",
  "purchase_token": "",
  "subscription_id": ""
}

json_payload = json.dumps(payload)

# url = 'https://chatgpt.vulcanlabs.co/api/v3/chat'

url = 'https://chatgpt-au.vulcanlabs.co/api/v1/token'

import requests

response = requests.post(url, headers=headers, data=json_payload)

print(response.status_code)
print(response.headers)
print(response.text)
print(type(response.text))
rstxt = json.loads(response.text)
print(rstxt)