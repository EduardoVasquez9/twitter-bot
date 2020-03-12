import tweepy
import os
import time
import random
import data

CONSUMER_KEY = 'EzxPAErQKKuxOj9ixHDsf6fY8'
CONSUMER_SECRET = 'Y0o5LcIwj8oRrv2Ioq5HRVp9iVfHknhZviR5xZI9ZphaVg6BgH'
ACCESS_KEY = '561631104-cjwYw5K4wh1VluRuXbfGgDt4HVVlQZl0coUs1qMH'
ACCESS_SECRET = 'caNU6qujBBWJhDsiwGqw5QtWxCv4tI2OqU0TvjF2SorV4'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
