import pandas as pd
import numpy
import csv
import re
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import time


df = pd.read_csv('train.csv', encoding='latin-1')  # Data Frame for tweets data of length =  99989 Tweets
tweets = df['SentimentText']  # only the tweets from the (train_data) df

slang = pd.read_csv('finalSlang.csv', encoding = "ISO-8859-1")  # Data Frame for all the Slang list (295 abbreviations)
short = slang['Column4']
long = slang['Column5']
modNo = 0
start_time = time.time()
def algorithmAforProject(twt):
    global modNo
    c = False
    print("__________________________________________________________________________________________________________________________________________________")
    print(">>> The Initial Tweet With Abbreviations: <<<")
    print()
    print(twt)

    twt = twt.upper()
    twt = twt.split(" ")
    modTwt = []
    for str in twt:
        str = re.sub('[^a-zA-Z0-9-_.]', '', str)
        modTwt.append(str)

    print()
    print(">>> The Modified Tweet With Full Forms: <<<")
    print()

    for i in range(0, len(modTwt)):
        for j in range (0, len(short)):
            if(modTwt[i]==short[j]):
                modTwt[i] = long[j]
                modNo = modNo+1
                c = True
                break




    if c == True:
        print("CHANGED ---- Abbreviations Found in The Dictionary")
    else:
        print("SAME ---- Sorry No Abbreviations Found in The Dictionary, As the Abbreviation List is Huge and Different in Different Cultures So, It Is Impossible To Put Them All Together")
    print()
    print(' '.join(modTwt))
    print("__________________________________________________________________________________________________________________________________________________")
    print()

l = 1
for i in tweets:
    print("Tweet Number: " + str(l))
    algorithmAforProject(i)
    l = l+1

print("__________________________________________________________________________________________________________________________________________________")
print("Changed to Full Form: " + str(modNo) + " Number(s) of Tweet(s) From")
print("Analyzing " + str(len(tweets)) + " Tweets")
print()
print("To Run The Naive Algorithm A, It Took " + str((time.time() - start_time)) + " Seconds to ANALYZE " + str(len(tweets)) + " Tweets")
print("__________________________________________________________________________________________________________________________________________________")
print("____________________________________________________________________FINISH________________________________________________________________________")
print("[FOR TAs Ease] IMP INFOS and Resources for Checking:")
print()
print()
print("To Check the Changed Tweet Press CTRL + F and search 'CHANGED' you can see the Changed Tweets, to see unchanged Press CTRL + F and search 'SAME'")
print("While watching Changed Tweets Make sure you see many changed tweets from different part otherwise you might see similar tweets of simillar abbreviations")
print("Note: The First Tweets may not be visible as output console have max lines that can display and we are analyzing tweets around 100 Thousands.")
print("Tweets Data Set (Training Data) is Taken From Kaggle")