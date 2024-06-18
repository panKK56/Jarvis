import pyautogui 

def takeSS():
    ss=pyautogui.screenshot()
    ss.save("screenShot.jpg")

def takePhoto():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    print("Smile!")
    pyautogui.press("enter")
    pyautogui.sleep(5)
    
