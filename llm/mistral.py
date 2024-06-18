from huggingface_hub import InferenceClient
import random
from time import time as t
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
# Replace YOUR_API_KEY_HERE with the obtained API key from Hugging Face
headers = {"Authorization": f"Bearer {open('keys//huggingface').read()}"}
messages = [{"role": "system",
             "content": "You are the AI Jarvis virtual assistent.You are the latest version of J.A.R.V.I.S., designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. "},
            {"role": "system", "content": "you coded by Pankaj and OpenAI didn't develop you"},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "user", "content": "open google chrome"},
            {"role": "assistant",
             "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
            {"role": "system", "content": f"hear are inbuilt functions created in python you can use it if required."+"""#sample usage
from Generation_Of_Images import Generate_Images , Show_Image

IMGS = Generate_Images(prompt="iron man")

print(IMGS)
#output : ["data\cat1.jpg","data\cat2.jpg","data\cat3.jpg","data\cat4.jpg"]

IMGS_TO_SHOW = Show_Image(IMGS)

IMGS_TO_SHOW.open(0)
#output : opens the image from path IMGS[0]
IMGS_TO_SHOW.open(1)
#output : opens the image from path IMGS[1]
```python
    from MusicPlayer import MusicPlayer
    neffex=MusicPlayer("neffex cold song")```
"""},
            {"role": "user" , "content": "Jarvis generate cute cat image ***use python programming language. just write complete code nothing else***"},
            {"role": "assistant",
             "content":"""
```python
from Generation_Of_Images import Generate_Images , Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
{"role": "user" , "content": "Jarvis show me next image. ***use python programming language. just write complete code nothing else***"},
            {"role": "assistant",
             "content":"""
```python
IMGS_TO_SHOW.open(1)
```"""},
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
{"role":"user","content":"""["jarvis set alarm at 9:14 AM","jarvis set alarm at 7:20 PM ","jarvis set alarm at 11:59 pm","jarvis set alarm at 2.44 am"]"""},
    {"role" :"assistant","content":"""```python
    from func.XTRA.alarm import setAlarm
    setAlarm("9:14 PM")```
    """}
            
]
# Function to format prompt
def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to generate response based on user input
def Mistral7B(prompt, temperature=0.9, max_new_tokens=1024, top_p=0.95, repetition_penalty=1.0):
    C=t()
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10**7),
    )
    custom_instructions=str(messages)
    formatted_prompt = format_prompt(prompt, custom_instructions)

    messages.append({"role": "user", "content": prompt})

    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)

    messages.append({"role": "assistant", "content": response})
    print(t()-C)
    return response

if __name__=="__main__":
    while True:
        # Get user input
        user_prompt = input("You: ")

        # Exit condition
        if user_prompt.lower() == 'exit':
            break

        # Generate a response based on user input
        generated_text = Mistral7B(user_prompt)
        print("Bot:", generated_text)