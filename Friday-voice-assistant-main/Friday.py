# import Features.Nasa as nasa


# nasa.MarsImage()



import speech_recognition as sr
# from gtts import gTTS
import pyttsx3
import os
import multiprocessing
import uuid
import Features.chat_gpt_free



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


def main():
    # speak_lock = multiprocessing.Value('i', 0)
    conversation_id = None
    parent_id = None

    result_reply, conversation_id, parent_id = Features.chat_gpt_free.main_chatbot("Hi", conversation_id, parent_id)
    print(result_reply, flush=True)
    result_reply = None
    while True:
        query = recognize_speech()
        if query is not None:
            result_reply, conversation_id, parent_id = Features.chat_gpt_free.main_chatbot(query, conversation_id, parent_id)
        if result_reply is not None:
            # print(result_reply)
            # print(type(result_reply))

            speak(result_reply)
            # process_openai = multiprocessing.Process(target=speak, args=(result_reply_str))
            # process_openai.start()
            # process_openai.join()
            result_reply = None
        if query is not None and 'special' in query:
            print('it was something special')
        elif query is not None and ( 'bye' in query or 'exit' in query or 'goodbye' in query or 'good bye' in query):
            print('exiting program')
            exit()
        else:
            print('nothing special')

        # process_openai.join()
        # if 'special' in query:
        #     tts_sample = "hi there i am just saying this so that you can test your program"
        #     while True:
        #         if speak_lock == 1:
        #             pass
        #         else:
        #             if speak_lock == 0:
                            
        #                 process_special_query = multiprocessing.Process(target=speak, args=(tts_sample, speak_lock))
        #                 process_special_query.start()
        #                 break
        # else:
        #     print('looping again')




if __name__ == '__main__':
    main()
