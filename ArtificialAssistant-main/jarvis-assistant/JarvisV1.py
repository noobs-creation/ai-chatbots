from readMails import reading_emails
from cryptoNews import reading_crypto_news
from google_news import getting_news
from shorts_yt_upload import uploading_short_video

import speech_recognition as sr
import datetime
import calendar
import pyttsx3

speechEngine = pyttsx3.init('sapi5')

def speak(audio):
    speechEngine.say(audio)
    print(audio)
    speechEngine.runAndWait()

# function for speech to text
def takeCommand():
    recorder= sr.Recognizer()
    with sr.Microphone() as source:
        # adjust for ambient noise
        # recorder.adjust_for_ambient_noise(source)
        print("listening...")
        audio = recorder.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print("recognizing...")
        query = recorder.recognize_google(audio, language='en-US')
        q = query.lower()
        print(f"User said : {query}")
    except Exception as e:
        speak("Say that again, please!")
        return "none"
    return q


# function to get date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    dateSpeak = f"{month}-{day}-{year}"
    speak(dateSpeak)

# function to get time
def time():
    timeSpeak = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(timeSpeak)

# function for wishing me at the end exiting time
def wishMeAfterEnding():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Bye Sid! Have a nice day")
    elif 12 <= hour < 16:
        speak("Bye Sid! See you soon again")
    elif 16 <= hour < 20:
        speak("Bye Sid! Have fun")
    else:
        speak("Bye Sid! Good night")

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    year_now = now.year

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    # return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."
    return "It's " + week_now + ", " + ordinals[day_now - 1] + " " + months[month_now - 1] + ' ' + str(year_now) + "."


def wishMeBeforeBeginning():
    speak("welcome sir!")
    speak("The time is ")
    time()
    speak("Today's date is")
    date()
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, Sid")
    elif 12 <= hour < 16:
        speak("Good afternoon, Sid")
    else:
        speak("Good evening, Sid")
    speak("Jarvis at your service!")

if __name__ == "__main__":
    # speak(today_date())
    # wishMeBeforeBeginning()
    #speak("This is jarvis, Sid's assistant")
    while True:
        speak('How can I help you?')
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'go offline' in query or 'shutdown' in query or 'go to sleep mode' in query:
            wishMeAfterEnding()
            quit()

        elif 'sports news' in query:
            news_list = getting_news(topic='Sports')
            for news in news_list:
                speak(news['title'])
        
        elif 'business news' in query:
            news_list = getting_news(topic='Business')
            for news in news_list:
                speak(news['title'])
        
        elif 'entertainment news' in query:
            news_list = getting_news(topic='Entertainment')
            for news in news_list:
                speak(news['title'])
        
        elif 'technology news' in query:
            news_list = getting_news(topic='Technology')
            for news in news_list:
                speak(news['title'])

        elif 'covid news' in query:
            news_list = getting_news()
            for news in news_list:
                speak(news['title'])
        
        elif 'world sports news' in query:
            news_list = getting_news(topic='Sports', location='World')
            for news in news_list:
                speak(news['title'])
        
        elif 'world business news' in query:
            news_list = getting_news(topic='Business', location='World')
            for news in news_list:
                speak(news['title'])
        
        elif 'world entertainment news' in query:
            news_list = getting_news(topic='Entertainment', location='world')
            for news in news_list:
                speak(news['title'])
        
        elif 'world technology news' in query:
            news_list = getting_news(topic='Technology', location='World')
            for news in news_list:
                speak(news['title'])

        elif 'world covid news' in query:
            news_list = getting_news(location='World')
            for news in news_list:
                speak(news['title'])

        elif 'crypto news' in query:
            speak("Here's the latest crypto news")
            crypto_data = reading_crypto_news()

            # print(data['Data'])
            count = 0
            for d in crypto_data['Data']:
                count += 1
                # print(d['title'])
                speak(d['title'])
                # print(d['body'])
                # speak(d['body'])
                print()

                if count == 3:
                    break
        
        elif 'primary email' in query or 'new mails in primary account' in query or 'primary mail' in query or 'new email in primary account' in query:
            unread_emails = reading_emails('primary')
            for i in unread_emails:
                speak('Email from ')
                speak(i['from'])
                speak('Subject: ')
                speak(i['subject'])
                speak('Message: ')
                speak(i['snippet'])

        elif 'secondary email' in query or 'new mails in secondary account' in query or 'secondary mail' in query or 'new email in secondary account' in query:
            unread_emails = reading_emails('secondary')
            for i in unread_emails:
                speak('Email from ')
                speak(i['from'])
                speak('Subject: ')
                speak(i['subject'])
                speak('Message: ')
                speak(i['snippet'])
        
        elif 'third email' in query or 'new mails in third account' in query or 'third mail' in query or 'new email in third account' in query:
            unread_emails = reading_emails('tertiary')
            for i in unread_emails:
                speak('Email from ')
                speak(i['from'])
                speak('Subject: ')
                speak(i['subject'])
                speak('Message: ')
                speak(i['snippet'])

        elif 'create shorts' in query or 'upload short' in query:
            speak('Uploading shorts')
            uploading_short_video()
