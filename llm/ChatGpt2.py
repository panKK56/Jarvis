#pip install -U g4f
import g4f
#can we talk on call ?  
from time import time as t
messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Divyansh Shukla with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "system", "content": """```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="iron man")
print(IMGS)
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
IMGS_TO_SHOW.open(1)
```
```python
from func.Jukebox.YouTube import MusicPlayer
#taks song name and it stats playing music
ncs=MusicPlayer("ncs")
#any btw 0 - 100
ncs.Vol(30)
#pause or play
ncs.Play()
ncs.Pause()
#next song
ncs.Next()
#quit song
ncs.Quit()
```
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
    
```python
from toolkit.ChatGpt import ChatGpt
from toolkit.Mistral import Mistral7B
from toolkit.Filter import Filter

#u can use chat gpt its slow but its accurate
print(ChatGpt("essay on saving environment *under 100 words*"))
code=ChatGpt("python code to open google chrome ***use python programing language. just write complete code nothing else, also don't dare to use input function***")

# Filter return only python code from provided txt
exec(Filter(code))```

#u can use Mistral7B its fast but not much accurate it can work grate but only for small task not grater than 256 tokens
print(Mistral7B("hii",temperature=0.9))
```"""},
    {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
    {"role": "assistant", "content": """```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
    {"role": "user", "content": "Jarvis show me the next image"},
    {"role": "assistant", "content": """```python
IMGS_TO_SHOW.open(1)
```"""},
    {"role": "user", "content":"Jarvis play neffex cold"},
    {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""},
    {"role": "user", "content":"Jarvis write an essay on Python around 100 words and save it to a text file in my current working directory"},
    {"role": "assistant", "content":"""```python\nfrom toolkit.ChatGpt import ChatGpt\nres=ChatGpt("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```"""},
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
    {"role":"user","content":"""["jarvis send msg what are you doing to adrsh tmv on whatsapp ","jarvis send msg hey to adrsh tmv on whatsapp ","jarvis send msg hello to me on whatsapp "]"""},
    {"role" :"assistant","content":"""```python
    from social.whatsApp import sendMSG
    sendMSG("me","hello")```
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
        model="gpt-4-32k-0613",
        provider=g4f.Provider.You,
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

    A=input("jarvis open chrome")
    C=t()
    ChatGpt(A)
    
