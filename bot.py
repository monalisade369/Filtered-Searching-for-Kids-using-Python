import nltk
from nltk.tokenize import word_tokenize as wt
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.corpus import stopwords
import pandas as pd
import webbrowser
import colorama 
from colorama import Fore, Style
print(Fore.GREEN+"""
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    ____ ____ ____ ____    ____ ____ ____ ____ ____ _  _ _ _  _ ____    ____ ____ ____    _  _ _ ___  ____ 
| | | |___ |    |    |  | |\/| |___     |  |  |    [__  |__| |___ |___    [__  |___ |__| |__/ |    |__| | |\ | | __    |___ |  | |__/    |_/  | |  \ [__  
|_|_| |___ |___ |___ |__| |  | |___     |  |__|    ___] |  | |    |___    ___] |___ |  | |  \ |___ |  | | | \| |__]    |    |__| |  \    | \_ | |__/ ___] 
                                                                                                                                                          
""")
print("\n\n",Style.RESET_ALL)
print("Where do you want to search...\n1. Google\n2. You Tube")
inp=int(input("Choose a number : "))
while ((inp != 1 ) ):
    if(inp == 2):
        break
    else:
        inp=int(input("Input your choice correctly\nEnter a number between 1 and 2... : "))
file=pd.read_csv("bad_words.csv")
file.columns=["Words"]

message=str(input("What do you want to search\n").lower())

token=wt(message)

sw=set(stopwords.words('english'))
filtered_sw=[w for w in token if w not in sw]

pos=[pos_tag(filtered_sw)]

wnl=WordNetLemmatizer()
base_word=[wnl.lemmatize(word) for word in filtered_sw]

msg1=" ".join(base_word)

score=sia().polarity_scores(msg1)
analysis=1 if score["pos"]>0 or score["neu"]> 0 else 0
flag=0
if analysis:
    print("Thanks for speaking nicely!!!!")
    flag=1
else :
    print("Please Speak Nicely...\n")

if(flag==1):
    for w in base_word:
        if w in file.values:
            print("Try searching something else...")
            break
        else:
            flag=2
if(flag==2):
    message=message.replace(" ","+")
    if (inp==2):
        print("Safe search on you tube on...")
        url_YT="https://www.youtube.com/results?search_query="+message
        webbrowser.open_new_tab(url_YT)
    if (inp==1):
        print("Safe Google search is on ......")
        url_G="https://www.google.com/search?q="+message+"&rlz=1C1VDKB_enIN1011IN1011&oq="+message+"id=chrome&ie=UTF-8"
        webbrowser.open_new_tab(url_G)


