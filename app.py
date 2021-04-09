import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib as sl
from em import *

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
    
    speak("I am Boss Please tell me how can I help you")

def sendmail(to,content):
    server = sl.SMTP("smtp.gmail.com",587)
    server.ehlo() #connect server to gemail server
    server.starttls() #to provide security
    server.login(e,p)
    server.sendmail(e,to,content)
    server.close()

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
    
    
def sendmail(to,content):
    server = sl.SMTP("smtp.gmail.com",587)
    server.ehlo() #connect server to gemail server
    server.starttls() #to provide security
    server.login(e,p)
    server.sendmail(e,to,content)
    server.close()

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

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pandeynaman23082000@gmail.com"
                sendmail(to,content) 
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send email.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google')
        

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" The time is {strTime}")
        
        elif 'thankyou' in query:
            speak('Welcome')

        elif 'what your name' in query:
            speak('I am Boss')