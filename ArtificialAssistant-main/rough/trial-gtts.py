from gtts import gTTS
from io import BytesIO

# tts = gTTS('hello', lang='en', tld='com.au')

# tts.save('hello.mp3')

mp3_fp = BytesIO()
tts = gTTS('hello master how are you', lang='en', tld='com.au')
tts.write_to_fp(mp3_fp)