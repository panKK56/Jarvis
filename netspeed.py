import speedtest
from  func.Speak.SpeakOffline2 import Speak

def checkSpeed():
    try:
        Speak("Wait network diagnostic is running.")
        wifi=speedtest.Speedtest()
        upload_speed=wifi.upload()/1048576
        download_speed=wifi.download()/1048576
        Speak(f"Wifi upload speed is {upload_speed}")
        Speak(f"Wifi download speed is {download_speed}")
    except:
        Speak("Unable to connect server right now, Try afterwords!")

