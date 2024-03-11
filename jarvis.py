import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for male ... 1 for female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<=12):
        speak("Good Morning Sir!")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon Sir!")
    elif (hour>= 18 and hour<20):
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("My name is Jarvis. Please tell me how may I help you")

def takeCommand(): # It takes michrophone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Coudln't recognize, say that again please....")
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            print("Alright!!!")
            speak("Alright")
            speak("According to  Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube......')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google......')
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak('Opening Gmail......')
            webbrowser.open("gmail.com")

        elif 'open facebook' in query:
            speak('Opening Facebook......')
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak('Opening Instagram......')
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'C:\\Complete Web Development Bootcamp\\Spotify Clone\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak('Opening VScode......')
            codePath = "C:\\Users\\suvoc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak("I am Javrvis. I am Your AI Voice Assistant")

        elif 'quit' in query:
            print("Quitting sir. Thanks for your time.")
            speak("Quitting sir. Thanks for your time.")
            exit()