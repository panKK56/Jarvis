from func.Speak.SpeakOffline2 import Speak
def rememberMSG(query):
    remember=open("remember.txt","a")
    remember.write(query)
    remember.close()
    Speak("Remembered sir!,What next sir.")
    return True
def rememberedInfo():
    remember=open("remember.txt","r")
    Speak(f"You told me {remember.read()}.")
    remember.close()
    return True

