# c3d211cb92fe444492adc1bf751626ca
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)
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