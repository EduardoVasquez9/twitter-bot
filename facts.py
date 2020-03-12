import tweepy
import os
import time
import random
from data import *

numberofTweets = 2
x=1
while numberofTweets >= x:
    for tweet in tweepy.Cursor(api.search, q="WhatTheFFacts").items():
        if tweet.user.name == 'What The F*** Facts':
            tweet.retweet()
            x+=1
            print(f'"{tweet.text}" was retweeted')
