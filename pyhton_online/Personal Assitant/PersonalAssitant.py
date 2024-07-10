import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from functools import reduce
import os
import webbrowser
import pywhatkit as kt
import pyjokes
import pyautogui
import time
import requests
import json

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    #This is a function for speaking.
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    #This is the first function to run and it is for wishing the user
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning Sir")
    elif(hour>12 and hour<=18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("Its Hope, how can I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")      
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query

def aritmetic(str):
    #This function performs arithmetic calculations
    try:
        numbers = []
        for word in str.split():
            if word.isdigit():
                numbers.append(float(word))
        if 'add' in str:
            result= sum(numbers)
            speak("Result is")
            print(result)
            speak(result)            
        elif 'subtract' in str:
            result= (numbers[0]-numbers[1])
            speak("Result is")
            print(result)
            speak(result)
        elif 'multiply' in str:
            result= reduce((lambda x,y:x*y),numbers)
            speak("Result is")
            print(result)
            speak(result)
        elif 'divide' in str:
            result= (round(numbers[0]/numbers[1],2))
            speak("Result is")
            print(result)
            speak(result)
    except Exception as e:
        speak("Please say that again")

def writedoc():
    speak("What type of file you want to write in, MsWord or text file or notepad")

def playmus():
    #plays music
    music_dir = "B:\\audios"
    songs = os.listdir(music_dir)
    # rd = random.choice(songs)
    for song in songs:
        if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir, song))

def timer():
    #sets the timer or stopwatch
    speak("For how many minutes?")
    timing = takeCommand()
    timing =timing.replace('minutes', '')
    timing = timing.replace('minute', '')
    timing = timing.replace('for', '')
    timing = float(timing)
    timing = timing * 60
    speak(f'I will remind you in {timing} seconds')
    time.sleep(timing)
    speak('Your time has been finished sir')

def news():
    speak("news for today are")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=c3d211cb92fe444492adc1bf751626ca"
    news=requests.get(url).text
    news_js=json.loads(news)
    arts=news_js["articles"]
    for article in arts:
        speak(article["title"])
        print(article["title"])
        speak("Next news is")
    speak("Thank for listning")

 
if __name__ == "__main__":
    # speak("Sparsh Bamrara is awesome")
    # speak("Hope")
    # wishMe()
    # while True:
        query=takeCommand().lower()
        if 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')
        
        # elif "add" in query or "subtract" in query or "divide" in query or "multiply" in query:          
        #     aritmetic(query)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        

        # elif "write a document" or "create a document"  in query:
        #     writedoc()

        if "a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # elif "open command prompt" in query:
        #     os.system("start cmd")

        # elif "shut down the system" in query:
        #     os.system("shutdown /s /t 5")

        # elif "restart the system" in query:
        #     os.system("shutdown /r /t 5")

        # elif "sleep the system" in query:
        #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        # elif 'switch the window' in query:
        #     pyautogui.keyDown("alt")
        #     pyautogui.press("tab")
        #     time.sleep(1)
        #     pyautogui.keyUp("alt")
        
        # elif "open facebook" in query:
        #     webbrowser.open("www.facebook.com")

        # elif "open stackoverflow" in query:
        #     webbrowser.open("www.stackoverflow.com")

        # elif "ip address" in query:
        #     ip =requests.get('https://api.ipify.org').text
        #     speak(f"your IP address is {ip}")
        
        elif "play music" or "play song" in query:
            playmus()

        # elif 'timer' in query or 'stopwatch' in query:
        #    timer()
        
        elif 'tell me news' in query:
            speak("please wait sir, feteching the latest news")
            news()
        
        elif "wikipedia" or "meaning of" in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open google" or "search for" in query:
            speak("Can you please repeat what you want to search for ")
            sear=takeCommand().lower()
            kt.search(sear)
