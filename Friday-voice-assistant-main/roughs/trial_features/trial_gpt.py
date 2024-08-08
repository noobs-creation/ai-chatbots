import pyttsx3

def Speak(audio, lock):
    lock.value = 1
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    print(f"recorded : {audio}")
    engine.say(audio)
    engine.runAndWait()
    lock.value == 0


def main_gpt(stri):
    let_str = 'hello there'
    Speak(let_str)
    Speak(stri)

