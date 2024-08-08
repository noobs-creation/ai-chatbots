from vlc import EventType, Media, MediaPlayer, MediaParseFlag, Meta
import json
import time
import speech_recognition as sr
import random

def _media_cb(event, *unused):
    # XXX callback ... never called
    print(event)

def takeCommand():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        # adjust for ambient noise
        # recorder.adjust_for_ambient_noise(source)
        print("listening...")
        audio = recorder.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print("recognizing...")
        query = recorder.recognize_google(audio, language='en-IN')
        print(f"User said : {query}")
    except Exception as e:
        print("Say that again, please!")
        return "none"
    return query

p = MediaPlayer()
# cmd1 = "sout=file/ts:%s" % outfile

# Opening JSON file
f = open('final-radio-browser.json', "rb")
 
# returns JSON object as
# a dictionary
data = json.load(f)

while True:
    searchtext = takeCommand().lower()
    if "hindi" in searchtext:
        i = data['final-list'][random.randint(0, len(data['final-list']) - 1)]
        for i in data['final-list']:
            if i['language'].lower() == "hindi":
                print(i['url'])
                media = Media(i['url'])
                p.set_media(media)
                p.play()
                while True:
                    inputtext = takeCommand().lower()
                    if "stop" in inputtext:
                        p.stop()
                        break
                break


# for i in data['final-list']:
#     # play_length = 60
#     url = i['url']
#     print(i)
#     time.sleep(3)
#     media = Media(url)  # , cmd1)

#     # media.get_mrl()
#     p.set_media(media)
#     p.play()
#     time.sleep(3)
#     while True:
#         inputtext = takeCommand()
#         if "stop" in inputtext:
#             p.stop()
#             break
    # e = p.event_manager()
    # e.event_attach(EventType.MediaMetaChanged, _media_cb, media)
    # e.event_attach(EventType.MediaParsedChanged, _media_cb, media)
    # meta = {Meta.Album: None,
    #         Meta.Genre: None,
    #         Meta.NowPlaying: None,
    #         Meta.Title: None,
    #         Meta.ShowName: None,}
    # print(media.get_meta(Meta.Album),media.get_meta(Meta.Genre),media.get_meta(Meta.NowPlaying))
    # time.sleep(5)
    # while True:  # loop forever
    #     # XXX using MediaParseFlag.local is not any different
    #     media.parse_with_options(MediaParseFlag.network, 2)  # 2 sec timeout

    #     inputtext = takeCommand()
    #     if "stop" in inputtext:
    #         break