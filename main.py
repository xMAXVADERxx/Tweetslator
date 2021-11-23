import tweepy
import dotenv
from googletrans import Translator
import random

translator = Translator()

file = open("GoogleCodes", "r")
codes = file.readlines()
for x in range(len(codes)):
    codes[x] = codes[x].strip()

def randTrans(str, list):
    translation = translator.translate(str, dest=list[random.randint(0,len(list)-1)])
    return translation


#get access tokens
config = dotenv.dotenv_values(".env")
CONSUMER_KEY = config["CONSKEY"]
CONSUMER_SECRET = config["CONSSECRET"]
ACCESS_TOKEN = config["ACCTOK"]
ACCESS_TOKEN_SECRET = config["ACCTOKSEC"]
BEARER = config["BEARER"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#create a client
client = tweepy.Client(BEARER, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#client.create_tweet(text="Test Tweet, pls ignore")



translation = randTrans("Hello, there!", codes)
print(translation.text)

