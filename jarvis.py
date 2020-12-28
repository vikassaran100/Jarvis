import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
#print(voices[0].id)
   

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak('Good Morning!')
    elif hour >= 12 and hour <18:
        speak('Good Aftrnoon')
    else:
        speak('Good Evening')

    speak("I am Jarvis , please Tell me How Can I help You")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconizing...')
        query = r.recognize_google(audio, language= 'en-in')
        print(f'User Said: {query}\n')

    except Exception as e:
       # print(e)

        print('please say that again...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikassaran100@gmail.com', "vvvVVV123")
    server.sendmail('saranvikas80@gmail.com', to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query =takeCommand().lower()
    #logic for executing task based on query
        if "wikipedia" in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak('according to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open Google' in query:
            webbrowser.open('google.com')

        elif 'open clc' in query:
            webbrowser.open('clc.com')

        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\Jarvis\\jarvis.py'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir, the time is {strtime}')

        elif 'open code' in query:
            codepath = "C:\\Users\\MAHAVEER PRASAD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email to vikas' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = 'saranvikas80@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!.')
            except Exception as e:
                print(e)
                speak('Sorry Sir, I am not able to send this email')

        elif 'exit' in query:
            exit()
            




