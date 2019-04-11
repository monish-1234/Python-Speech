# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:51:44 2019

@author: Monish
"""
import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source, timeout=3, phrase_time_limit=3)   

try:
    print("You said " + r.recognize_google(audio))
    meh=("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results . Check Your Internet Connection ; {0}".format(e))
    
# Speaking it back 
    
import pyttsx3

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.say(meh)

engine.runAndWait()
