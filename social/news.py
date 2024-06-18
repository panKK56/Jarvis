import requests
import html

KEY=open("keys//news").read()

def remove_special_characters(text):
    try:
        cleaned_text = text.encode('ascii', 'ignore').decode('ascii')
        return cleaned_text
    except:
        return "Contains special characters!"

def clean_news_headlines(headlines):
    try:
        cleaned_headlines = []
        for headline in headlines:
            # Decode HTML entities
            decoded_headline = html.unescape(headline)
            # Remove unwanted phrases or words
            cleaned_headline = decoded_headline.replace('Deal Dive:', '').replace('TC+ Roundup:', '')
            # Append the cleaned headline to the list
            cleaned_headlines.append(cleaned_headline)
        return cleaned_headlines
    except:
        return "Not able clean headlines!"

def News()->str:
    try:
        global KEY
        main_url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={KEY}'
        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
        for ar in articles:
            head.append(ar["title"])
        temp=[]
        for i in range (len(day)):
            temp.append(f"today's {day[i]} news is: {head[i]}\n")
        temp=clean_news_headlines(temp)
        r=""
        for i in temp:
            r+=i
        return r
    except:
        return "Can't able to find news!"

if __name__=="__main__":
    print(News())
