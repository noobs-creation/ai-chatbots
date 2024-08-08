import requests

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

# querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":"Hello!"}

headers = {
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
    'x-rapidapi-key': "62c2b7fb91msh963773aad27380ep1f324ejsnaea42d3980c0"
    }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

while True:
    msg = input("Enter your message: ")
    querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":msg}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)