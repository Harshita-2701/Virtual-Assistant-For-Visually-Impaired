import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout



class Grid_LayoutApp(App):


   def build(self):


      layout = GridLayout(cols = 2)


      layout.add_widget(Button(text ='Call'))
      layout.add_widget(Button(text ='time & date'))

      # 2nd row
      layout.add_widget(Button(text ='message'))
      layout.add_widget(Button(text ='location'))

      # 3rd row
      layout.add_widget(Button(text ='face detection'))
      layout.add_widget(Button(text ='currency detection'))



      # returning the layout
      return layout

# creating object of the App class
root = Grid_LayoutApp()

# run the App
root.build()
root.run()
import speech.py

speech.record_audio()
speech.respond()
os.system("python speech.py ")

import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
    voice_msg = ''
    try:
        voice_msg = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak('Sorry,I did not get that')
    except sr.RequestError:
        speak('Sorry,my speech service is down')
    return voice_msg


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_msg):
    if 'what time is it' in voice_msg:
        speak(ctime())
    elif 'find location' in voice_msg:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    elif 'call' in voice_msg:
        speak("do u want to call?")
        speak("enter the phone number")
        import call
        call.call()
        speak("your call has been placed")
        os.system("python call.py ")
    elif 'location' in voice_msg:
        speak("enter the phone number")
        import location
        os.system("python location.py ")
        

    elif 'message' in voice_msg:
        speak("do u want to message someone?")
        speak("enter the phone number")
        import message
        message.message()
        speak("message has been sent")
        os.system("python message.py ")
    elif 'face' in voice_msg:
        speak("here is the your face detection")
        import face
        os.system("python face.py ")
    elif 'currency' in voice_msg:
        speak("detect your currency")
        import app
        os.system("python app.py ")
    elif 'exit' in voice_msg:
        exit()


time.sleep(1)
speak('how can i help u?')
while 1:
    voice_msg = record_audio()
    respond(voice_msg)
