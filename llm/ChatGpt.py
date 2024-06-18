#pip install -U g4f
#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 ----api key
import g4f
import warnings
#can we talk on call ?  
from time import time as t

import g4f.Provider
import g4f.Provider.you
warnings.filterwarnings("ignore")
messages = [
     {"role": "system",
             "content": "You are the AI Jarvis virtual assistent.You are the latest version of J.A.R.V.I.S., designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. "},
            {"role": "system", "content": "you coded by Pankaj "},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "user", "content": "open google chrome"},
            {"role": "assistant",
             "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
            {"role": "system", "content": f"hear are inbuilt functions created in python you can use it if required."+"""#sample usage
    ```python
        from social.whatsApp import sendMSG
        sendMSG("adrsh","what are you doing")```      
    ```python
        from MusicPlayer import MusicPlayer
        neffex=MusicPlayer("neffex cold song")```
    ```python
        from func.XTRA.setAlarm import runAlarm
        runAlarm("20:12:00")``` 
    ```python
    from func.XTRA.smartBulb import turn_on_bulb
    turn_on_bulb()```
     ```python
    from func.XTRA.smartBulb import turn_off_bulb
    turn_off_bulb()``` 
    ```python
    from reMEMber import rememberMSG
    rememberMSG("I have meeting tommarow.")```
    ```python
    from reMEMber import rememberedInfo
    rememberedInfo()```
    ```python
    from func.XTRA.volumeUpDown import volumeUp
    volumeUp()```
    ```python
    from func.XTRA.volumeUpDown import volumeDown
    volumeDown()```
    ```python
    from netspeed import checkSpeed
    checkSpeed()```
    ```python
    from func.XTRA.camera import takeSS
    takeSS()```
    ```python
    from func.XTRA.camera import takePhoto
    takePhoto()``` 
    """},
    {"role": "user", "content":"Jarvis play music neffex cold by my function"},
    {"role": "assistant", "content":"""```python
    from MusicPlayer import MusicPlayer
    neffex=MusicPlayer("neffex cold song")```"""},   
    {"role":"user","content":"""["jarvis play music destiny  by my function","jarvis play song ncs by my function","jarvis play song neffex by my function","play music barishein by my function","play music destiny by my function"]"""},
    {"role" :"assistant","content":"""```python
    from MusicPlayer import MusicPlayer
    #taks song name and it stats playing music
    ncs=MusicPlayer("ncs")```
    """},
    {"role":"user","content":"""["jarvis send msg what are you doing to adrsh tmv on whatsapp ","jarvis send msg hey to adrsh tmv on whatsapp ","jarvis send msg hello to me on whatsapp "]"""},
    {"role" :"assistant","content":"""```python
    from social.whatsApp import sendMSG
    sendMSG("adrsh","what are you doing")```
    """},
    {"role":"user","content":"""["jarvis send msg what are you doing to adrsh tmv on whatsapp","jarvis send msg hey to adrsh tmv on whatsapp ","jarvis send msg hello to sushant on whatsapp "]"""},
    {"role" :"assistant","content":"""```python
    from social.whatsApp import sendMSG
    sendMSG("adrsh","what are you doing")```
    """},
    {"role":"user","content":"""["jarvis todays news","jarvis top news today ","todays news"]"""},
    {"role" :"assistant","content":"""```python
    from social.news import News
    print(News())```
    """},
    {"role":"user","content":"""["jarvis set alarm at 9:14 AM","jarvis set alarm at 7:20 PM ","jarvis set alarm at 11:59 p.m.","jarvis set alarm at 2.44 a.m"]"""},
    {"role" :"assistant","content":"""```python
    from func.XTRA.setAlarm import runAlarm
    runAlarm("20:12:00")```
    """},
    {"role": "user", "content":"Jarvis turn on light"},
    {"role": "assistant", "content":"""```python
    from func.XTRA.smartBulb import turn_on_bulb
    turn_on_bulb()```"""},
    {"role": "user", "content":"Jarvis turn off light"},
    {"role": "assistant", "content":"""```python
    from func.XTRA.smartBulb import turn_off_bulb
    turn_off_bulb()```"""},
    {"role": "user", "content":"Jarvis remember I have meeting tommarow."},
    {"role": "assistant", "content":"""```python
    from reMEMber import rememberMSG
    rememberMSG("I have meeting tommarow.")```"""},
    {"role": "user", "content":"Jarvis whats the reminder."},
    {"role": "assistant", "content":"""```python
    from reMEMber import rememberedInfo
    rememberedInfo()```"""},
    {"role": "user", "content":"""["Jarvis volumeup","jarvis volume up"]"""},
    {"role": "assistant", "content":"""```python
    from func.XTRA.volumeUpDown import volumeUp
    volumeUp()```"""},
    {"role": "user", "content":"""["Jarvis volumedown","jarvis volume down"]"""},
    {"role": "assistant", "content":"""```python
    from func.XTRA.volumeUpDown import volumeDown
    volumeDown()```"""},
    {"role": "user", "content":"""jarvis check internet speed"""},
    {"role": "assistant", "content":"""```python
    from netspeed import checkSpeed
    checkSpeed()```"""},
    {"role": "user", "content":"""jarvis take screenshot"""},
    {"role": "assistant", "content":"""```python
    from func.XTRA.camera import takeSS
    takeSS()```"""}, 
    {"role": "user", "content":"""jarvis take photo"""},
    {"role": "assistant", "content":"""```python
    from func.XTRA.camera import takePhoto
    takePhoto()```"""}      
]

def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x>5500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None

def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    MsgDelAuto()
    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model='gpt-4-turbo',#"gpt-4-32k-0613", gpt-3.5-turbo, gpt-4-plus,gpt-4-turbo,gpt-4
        provider=g4f.Provider.You, # bing gpt -4 -turbo
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":
    # while 1:
        A="create power point presentation on coffee"#'create power point presentation on coffee'#'create snake game'#"jarvis send msg what are you doing to adrsh"
        C=t()
        ChatGpt(A)
        print(t()-C)

