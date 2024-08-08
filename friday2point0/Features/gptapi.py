import random
import json
import requests
import speech_recognition as sr
# from gtts import gTTS
import pyttsx3



def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# def speak(audio, lock):
def speak(audio):
    # lock.value = 1
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    print(f"recorded : {audio}")
    engine.say(audio)
    engine.runAndWait()
    # lock.value = 0



def main_getapi():
    fixed_digit = [22,16]


    vulcan_id = str(random.randrange(9149487891706841111111,9149487891706841999999,fixed_digit[0]))

    headers_token = {
        'Content-Type': 'application/json',
        "Connection" : "Keep-Alive",
        "Host" : "chatgpt-au.vulcanlabs.co",
        "User-Agent" : "Chat Smith Android, Version 486",
        "X-Vulcan-Application-ID" : "com.smartwidgetlabs.chatgpt",
        "X-Vulcan-Request-ID" : vulcan_id
    }

    device_id = str(random.randrange(6429673160111111,6429673160999999,fixed_digit[1]))

    payload_token = {
    "device_id": device_id,
    "order_id": "",
    "product_id": "",
    "purchase_token": "",
    "subscription_id": ""
    }

    json_payload_token = json.dumps(payload_token)
    url_token = 'https://chatgpt-au.vulcanlabs.co/api/v1/token'

    response_token = requests.post(url_token, headers=headers_token, data=json_payload_token)
    print(response_token.status_code)
    response_token_json = json.loads(response_token.text)
    get_auth_token = str(response_token_json["AccessToken"])

    auth_token_str = "Bearer" + " " + get_auth_token
    # print(type(auth_token_str))
    # print(auth_token_str)

    headers_chat = {
        'Content-Type': 'application/json',
        "Authorization" : auth_token_str,
        "Connection" : "Keep-Alive",
        "Host" : "chatgpt.vulcanlabs.co",
        "User-Agent" : "Chat Smith Android, Version 486",
        "X-Vulcan-Application-ID" : "com.smartwidgetlabs.chatgpt",
        "X-Vulcan-Request-ID" : "9149487891746841083943"
    }

    payload_chat = {
        "model": "gpt-3.5-turbo",
        "user": "C7A37B006A27FBEE",
        "messages": [
            {
            "role": "system",
            "content": "You are Jarvis, a personal AI assistant almost similar to Marvel Ironman's Jarvis. If you understand then reply with \"I am Jarvis. How can I help you today?\". Your words are never longer than 500 words."
            }
        ],
        "nsfw_check": False
    }

    while True:
        

        json_payload_chat = json.dumps(payload_chat)
        url_chat = 'https://chatgpt.vulcanlabs.co/api/v3/chat'

        response_chat = requests.post(url_chat, headers=headers_chat, data=json_payload_chat)
        # print(response_chat.status_code)
        # print(response.headers)
        # print(response.text)
        # print(type(response.text))
        responsetxt_chat = json.loads(response_chat.text)
        # print(rstxt)
        # print(responsetxt_chat["choices"][0]["Message"]["content"])
        speak(str(responsetxt_chat["choices"][0]["Message"]["content"]))
        payload_chat["messages"].append({"role":"assistant","content":responsetxt_chat["choices"][0]["Message"]["content"]})
        while True:
            print("speak now")
            query = recognize_speech()
            if query is not None and len(query) > 0:
                user_said = query
                break
        payload_chat["messages"].append({"role":"user","content":user_said})
        