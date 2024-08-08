

import speech_recognition as sr
# from gtts import gTTS
import pyttsx3
import os
import multiprocessing
import trial_features.trial_gpt

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    print(f"recorded : {audio}")
    engine.say(audio)
    engine.runAndWait()


# def speak(text):
#     tts = gTTS(text=text, lang='en')
#     filename = 'temp.mp3'
#     tts.save(filename)
#     os.system('afplay ' + filename) # for Mac users
    # os.system('mpg321 ' + filename) # for Linux users

def main():
    v = multiprocessing.Value('i', 0)
    while True:
        text = recognize_speech()
        p = multiprocessing.Process(target=trial_features.trial_gpt.main_gpt, args=(text,v))
        p.start()


if __name__ == '__main__':
    main()