
from time import sleep
from selenium.webdriver.common.by import By
from func.Speak.SpeakOffline2 import Speak
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import warnings
warnings.simplefilter('ignore')

webdriver_path = "C:\\Users\\panka\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
ScriptDir = pathlib.Path().absolute()

# Use undetected_chromedriver
# Use undetected_chromedriver
options = uc.ChromeOptions()
# options.add_argument("--no-sandbox")  # Required for Linux
# options.add_argument("--disable-dev-shm-usage")
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={ScriptDir}\\chromedata')
driver = uc.Chrome(driver_executable_path=webdriver_path,options=options)
driver.maximize_window()


sleep(4)


class MusicPlayer:
    global driver
    def __init__(self,VidName:str) -> None:
        self.Volume=100

        self.VidName=VidName
        self.VidName.replace("jarvis play music","")
        self.VidName.replace(" ","+")
        driver.get("https://www.youtube.com/results?search_query="+self.VidName+" song")
        sleep(1)
        xpath='//*[@id="thumbnail"]/yt-image/img'
        driver.find_element(By.XPATH,value=xpath).click()
        Speak("Task completed sir.")
        sleep(180)
        
#         def Vol(self,VolInt:int):
#             if VolInt > 100 or VolInt < 0:
#                 return "MOYE MOYE"
#             #50 , 100 -5
#             #50 = 100 - (x * 5)
#             if VolInt>self.Volume:
#                 #VolInt = volume + (x*5)
#                 #(VolInt-Volume)/5=x
#                 steps=(VolInt-self.Volume)//5
#                 self.Volume=VolInt
#                 video = driver.find_element(By.CLASS_NAME,"html5-video-player")
#                 for _ in range(steps):
#                     sleep(0.1)
#                     video.send_keys(Keys.UP)
#             else:
#                 #VolInt = volume + (x*5)
#                 #(VolInt-Volume)/5=x
#                 steps=(VolInt-self.Volume)//-5
#                 self.Volume=VolInt
#                 video = driver.find_element(By.CLASS_NAME,"html5-video-player")
#                 for _ in range(steps):
#                     sleep(0.1)
#                     video.send_keys(Keys.DOWN)
    def PauseOrPlay(self):
        # driver.find_element(By.CLASS_NAME,"html5-video-player").click()
        pass

    def Next(self):
        x=driver.find_element(By.CLASS_NAME,"html5-video-player")
        x.send_keys(Keys.SHIFT, 'n') 

    def Stop(self):
        driver.close()
    def play(self):
        # driver.find_element(By.CLASS_NAME,"html5-video-player").click()
        pass
    def Pause(self):
        driver.find_element(By.CLASS_NAME,"html5-video-player").click()



if __name__=="__main__":
    ncs=MusicPlayer("ncs")
    while 1:
        pass