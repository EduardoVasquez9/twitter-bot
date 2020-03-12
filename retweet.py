import tweepy
import os
import time
import random
from data import *

search = str(input("Palabra clave:"))

numberofTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
    try:
        tweet.retweet()
        print("Retweeteado!")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
