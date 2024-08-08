headers = {

    # "accept" : "text/event-stream",
    "accept" : "application/json",
    # "Accept-Charset" : "UTF-8",
    "Accept-Encoding" : "gzip",
    "Connection" : "Keep-Alive",
    "content-type" : "application/json",
    # "Content-Type" : "application/json",
    "Host" : "aichat.youxiong.win",
    "User-Agent" : "Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.034)"
}

import json

payload = {
  "stream": True,
  "uuid": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d",
  "session_id": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d_1709782748239",
  "message": "What are the most common interview questions?",
  "history": [
    {
      "role": "user",
      "content": "What are the most common interview questions?"
    }
  ]
}


'''{
  "stream": True,
  "uuid": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d",
  "session_id": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d_1709782816029",
  "message": "how to face interviewers",
  "history": [
    {
      "role": "user",
      "content": "What are the most common interview questions?"
    },
    {
      "role": "user",
      "content": "how to face interviewers"
    }
  ]
}'''

'''{
  "stream": true,
  "uuid": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d",
  "session_id": "and@chatAI2@8ee04634-3973-47ab-b5eb-b318610cad2d_1709782748239",
  "message": "What are the most common interview questions?",
  "history": [
    {
      "role": "user",
      "content": "What are the most common interview questions?"
    }
  ]
}'''

json_payload = json.dumps(payload)

url = "https://aichat.youxiong.win/askai"

import requests


response = requests.post(url, headers=headers, data=json_payload)

print(response)
print(response.status_code)
print(response.headers)
print(response.text)
# print(type(response.text))
# rstxt = json.loads(response.text)
# print(rstxt)
# print(type(rstxt))

# s = requests.Session()

# with s.post(url, headers=headers, stream=True, data=json_payload) as resp:
#     print(resp)
#     print(type(resp))
#     for line in resp.iter_lines():
#         # print(line)
#         print(line.decode())
#         print(type(line))
#         l = json.loads(line.decode())
#         print(l)
#         print(type(l))
    # for line in resp.iter_lines():
    #     if line:
    #         print(line)