import tweepy
import dotenv
from googletrans import Translator
import datetime
import random
import time
import os

translator = Translator()

file = open("GoogleCodes", "r")
codes = file.readlines()
print(codes)
for x in range(len(codes)):
    codes[x] = codes[x].strip()
print(codes)

def trans(str, destLang=None):
    if destLang == None:
        destLang = codes[random.randint(0,len(codes)-1)]
    print(f"Destination Language Code: {destLang}")
    translation = translator.translate(str, dest=destLang)
    return translation


#get access tokens and config data
dotenv.load_dotenv()
CONSUMER_KEY = os.getenv("CONSKEY")
CONSUMER_SECRET = os.getenv("CONSSECRET")
ACCESS_TOKEN = os.getenv("ACCTOK")
ACCESS_TOKEN_SECRET = os.getenv("ACCTOKSEC")
BEARER = os.getenv("BEARER")
ID = os.getenv("SELF_ID")
try:
    updateTime = os.getenv("FIRSTTIME")
except all:
    updateTime = "2020-01-01T00:00:00Z"

#create a client
client = tweepy.Client(BEARER, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#uncomment to test client setup VV
#client.create_tweet(text="Test Tweet, pls ignore")

user = client.get_user(id=ID)

translation = trans("Hello, there!")
print(translation.text)

while True:
    
    #gets user mentions and tweets
    try:
        mentions = client.get_users_mentions(id=ID, start_time=updateTime)

    except tweepy.TweepyException:
        mentions = ["Empty"]
        print(mentions)

    try:
        tweets = client.get_users_tweets(id=ID)
    except tweepy.TweepyException:
        #if tweet can't be found, just grab my most recent tweet (@xmaxvaderxx, btw)
        tweets = client.get_users_tweets(id=2365430914, max_results=1)

    #outputs information to console
    try:
        print(f"{str(len(mentions[0]))} tweets mention @{user[0].name}")
        print(mentions)
    except all:
        print("No Mentions")
    

    #doing stuff with tweets
    for mention in mentions[0]:
        print(mention)
        if (not (mention in tweets[0])) and (mentions[0] != "Empty" ):
            text = mention.text
            
            #remove handle, frees up characterss
            text.replace("@TweetslatorBot","")
            translation = trans(text)
            #client.create_tweet(text=translation.text, in_reply_to_tweet_id=mention.id)

    #sets new timeframe, in order to prevent scanning and replying to already seen tweets
    date = datetime.datetime.now()
    updateTime = f"{str(date.year)}-{str(date.month)}-{str(date.day)}T{str(date.hour)}:{str(date.minute)}:{str(date.second)}Z"
    print(f"Update time: {updateTime}")

    #wait - saves system from dying and keeps bot within API limits
    time.sleep(15)