import pyttsx3
from gtts import gTTS
import os
import datetime


def offline_text_to_mp3(text, output_dir=None):
    return

def online_text_to_mp3(text, output_dir=None):
    tts = gTTS(text=text, lang='en')
    if output_dir == None:
        output_dir = ""
    time_now = datetime.datetime.now().strftime("%Y%m%d%H%M")
    out_file = f'otts_say-{time_now}.mp3'
    tts.save(f'{output_dir}{out_file}')

if __name__ == '__main__':

    online_text_to_mp3("Twitter is for the birds.")
    
    # engine = pyttsx3.init()
    # engine.say("Kenneth Bailey, welcome")
    # engine.runAndWait()