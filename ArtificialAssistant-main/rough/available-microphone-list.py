import speech_recognition as sr

print(sr.__version__)
print(sr.Microphone.list_microphone_names())

for i in sr.Microphone.list_microphone_names():
    print(i)