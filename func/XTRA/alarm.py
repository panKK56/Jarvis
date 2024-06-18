import datetime
# from func.Speak.SpeakOffline2 import Speak
import winsound
import threading

def setAlarm(Timing):
    alTime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    alTime=alTime[11:-3]
    hReal=alTime[:2]
    hReal=int(hReal)
    mReal=alTime[3:5]
    mReal=int(mReal)
    print(f"Done,Alarm is set for timing {Timing}")

    while True:
        if (hReal==datetime.datetime.now().hour):
            if mReal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif mReal<datetime.datetime.now().minute:
                break
    

if __name__=="__main__":
    setAlarm("9:52 PM")


