import time
import pygame
from threading import Thread

def setAlarm(alarm_time,sound_file):
    while True:
        current_time=time.strftime("%H:%M:%S")
        if current_time>=alarm_time:
            print("Time's up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break
        time.sleep(1)

def runAlarm(alarm_time,sound_file="temp\It_is_realme.mp3"):
    Thread(target=setAlarm,args=(alarm_time,sound_file)).start()

