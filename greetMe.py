from func.Speak.SpeakOffline2 import Speak
import datetime

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        Speak("Good Afternoon,pankaj")
    elif hour >12 and hour<=18:
        Speak("Good Afternoon ,pankaj")

    else:
        Speak("Good Evening,sushnat")

    Speak("I am jarvis,here to help you.")

if __name__=="__main__":
    greetMe()
