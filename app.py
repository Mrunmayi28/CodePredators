import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib as sl
from em import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from BossUi import Ui_BossUi 





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

def sendmail(to,content):
    server = sl.SMTP("smtp.gmail.com",587)
    server.ehlo() #connect server to gemail server
    server.starttls() #to provide security
    server.login(e,p)
    server.sendmail(e,to,content)
    server.close()



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def takeCommand(self):
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
    
    def TaskExecution(self):
        wishMe()

        while True:
            self.query = self.takeCommand().lower()

            if 'wikipedia' in self.query:
                speak("Searching Wikipedia....")
                query = query.replace("wikipedia", "")
                results= wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "mrun282002@gmail.com"
                    sendmail(to,content) 
                    speak("Email has been sent successfully!")
                except Exception as e:
                    print(e)
                    speak("Sorry I am not able to send email.")

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
                speak('opening youtube')
            
            elif 'open google' in self.query:
                speak("What should I search in google")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")
            

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f" The time is {strTime}")

            elif 'close' in self.query:
                exit()

startExecution = MainThread()

class Main(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BossUi()
        self.ui.setupUi(self) 
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("FBG.jpg") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        self.ui.movie = QtGui.QMovie("Fgif.gif") 
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        
app = QApplication(sys.argv)
Boss = Main()
Boss.show()
exit(app.exec_())