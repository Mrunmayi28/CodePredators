import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from BossGui import Ui_BossUi 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():          #Wishes  
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Alexa Please tell me how can I help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

def takeCommand():
    #Take Command from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

        

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)

        print("Say that again please....")
        speak("Say that again please")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google')
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")        #error (not Opening )
            speak('opening stackoverflow')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" The time is {strTime}")

        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16"
            os.startfile(wordPath)
        
        elif 'thankyou' in query:
            speak('Welcome')

        elif 'what your name' in query:
            speak('I am Alexa')