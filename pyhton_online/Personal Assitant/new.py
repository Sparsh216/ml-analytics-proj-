import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit as kit
from requests import get
import wikipedia
import webbrowser
import sys
import time
import pyjokes
import requests
import pyautogui
import os.path
import json
from functools import reduce

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    #This is a function for speaking.
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    #This is the first function to run and it is for wishing the user
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning Sir")
    elif(hour>12 and hour<=18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("Its Hope, how can I help you")

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

def sendEmail(to,content):
    #to send email
    kit.send_mail("test@gmail.com", "password", "Test Mail", "This is a test email", "testrecv@gmail.com")

def writedoc():
    speak("What type of file you want to write in, wordfile or text file")
    com=takecommand().lower()
    if "text file" in com:
        speak("Please speak the content of the file")
        content=takecommand().lower()
        content.capitalize()
        speak("Give a name to the file")
        name=takecommand().lower()
        name.capitalize()
        with open(f"{name}.txt","w") as f:
            f.write(content)
    elif "word file" in com:
        speak("Please speak the content of the file")
        content=takecommand().lower()
        content.capitalize()
        speak("Give a name to the file")
        name=takecommand().lower()
        name.capitalize()
        with open(f"{name}.docx","w") as f:
            f.write(content)

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

def playmus():
    #plays music
    music_dir = "B:\\audios"
    songs = os.listdir(music_dir)
    # rd = random.choice(songs)
    for song in songs:
        if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir, song))


if __name__ == "__main__": #main program
    wish()
    while True:
    # if 1:
        query = takecommand().lower()
        #logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "add" in query or "subtract" in query or "divide" in query or "multiply" in query:     
            aritmetic(query)
            
        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')
        
        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query or "play a song" in query:
             playmus()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query or "search for" in query:
            speak("Can you please repeat what you want to search for ")
            sear=takecommand().lower()
            kit.search(sear)

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+91_To_number_you_want_to_send", "this is testing protocol",4,13)
            time.sleep(120)
            speak("message has been sent")

        elif "song on youtube" in query:
            speak("Tell the name of song please")
            n=takecommand().lower()
            kit.playonyt(n)
            
        elif 'set timer' in query or 'set stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished sir')

#to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

#to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22: 
                music_dir = 'C:\\Users\\ANIRUDH\\Downloads\\Peaky Blinders_320(PaglaSongs)'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "write a document" in query or "create a document"  in query:
            writedoc()

        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()
            
        elif "no thanks" in query or "quit" in query or "thank you" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        
        elif "information" in query:
            speak("Tell me the topic")
            topic=takecommand().lower()
            kit.info(topic)