from time import sleep
from selenium.webdriver.common.by import By
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import warnings
warnings.simplefilter('ignore')

webdriver_path = "C:\\Users\\panka\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
ScriptDir = pathlib.Path().absolute()
url = "https://web.whatsapp.com/"

# Use undetected_chromedriver
options = uc.ChromeOptions()
# options.add_argument("--no-sandbox")  # Required for Linux
# options.add_argument("--disable-dev-shm-usage")
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={ScriptDir}\\chromedata')
driver = uc.Chrome(driver_executable_path=webdriver_path,options=options)
driver.maximize_window()
driver.get(url=url)
sleep(18)


def sendMSG(name:str,msg:str):
    search_box = driver.find_element("xpath", "//div[@contenteditable='true'][@data-tab='3']")
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    sleep(2)
    msgBox=driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    msgBox.clear()
    msgBox.send_keys(msg)
    sleep(1)
    driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    sleep(4)


# sendMSG("sushant","hooooo")





