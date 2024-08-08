headers = {
    'Content-Type': 'application/json',
    "Connection" : "Keep-Alive",
    "Host" : "chatgpt-au.vulcanlabs.co",
    "User-Agent" : "Chat Smith Android, Version 486",
    "X-Vulcan-Application-ID" : "com.smartwidgetlabs.chatgpt",
    "X-Vulcan-Request-ID" : "9149487891706841357145"
}

import json

payload = {
  "device_id": "6429673160507935",
  "order_id": "",
  "product_id": "",
  "purchase_token": "",
  "subscription_id": ""
}

json_payload = json.dumps(payload)

# url = 'https://chatgpt.vulcanlabs.co/api/v3/chat'

url_token = 'https://chatgpt-au.vulcanlabs.co/api/v1/token'

import requests

response = requests.post(url_token, headers=headers, data=json_payload)

print(response.status_code)
# print(response.headers)
# print(response.text)
# print(type(response.text))
rsp_token = json.loads(response.text)
auth_token = str(rsp_token["AccessToken"])
print(auth_token)

auth_token_str = "Bearer" + " " + auth_token
# print(type(auth_token_str))
print(auth_token_str)

headers = {
    'Content-Type': 'application/json',
    "Authorization" : auth_token_str,
    "Connection" : "Keep-Alive",
    "Host" : "chatgpt.vulcanlabs.co",
    "User-Agent" : "Chat Smith Android, Version 486",
    "X-Vulcan-Application-ID" : "com.smartwidgetlabs.chatgpt",
    "X-Vulcan-Request-ID" : "9149487891746841083943"
}

import json

payload = {
    "model": "gpt-3.5-turbo",
    "user": "C7A37B006A27FBEE",
    "messages": [
        {
        "role": "system",
        "content": "You are Chat Smith, a personal AI. Your words are never longer than 2000 words."
        }
    ],
    "nsfw_check": False
    }

while True:
    

    json_payload = json.dumps(payload)

    url = 'https://chatgpt.vulcanlabs.co/api/v3/chat'


    import requests

    response = requests.post(url, headers=headers, data=json_payload)

    print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(type(response.text))
    rstxt = json.loads(response.text)
    # print(rstxt)
    print(rstxt["choices"][0]["Message"]["content"])
    
    payload["messages"].append({"role":"assistant","content":rstxt["choices"][0]["Message"]["content"]})
    while True:
        user_said = str(input())
        if len(user_said) > 0:
            break
    payload["messages"].append({"role":"user","content":user_said})
    