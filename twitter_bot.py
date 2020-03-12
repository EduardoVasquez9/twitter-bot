import sys
import time
import telepot
import tweepy
from telepot.loop import MessageLoop
from validate_email import validate_email
import os
import random
import requests
from data import *

AUTHCHATS = {}
AUTTWEETS = {}
TOKEN = "894152792:AAF9F8dQwkLiGxdmbtRqCTC_Q1xHg7WE1pI"
bot = telepot.Bot(TOKEN)

AUTHCODE = "Unicah123"

AUTHWHAITING = []
AUTHDATA = []
TWEETWHAITHING= []


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	CONSUMER_KEY = 'EzxPAErQKKuxOj9ixHDsf6fY8'
	CONSUMER_SECRET = 'Y0o5LcIwj8oRrv2Ioq5HRVp9iVfHknhZviR5xZI9ZphaVg6BgH'
	ACCESS_KEY = '561631104-cjwYw5K4wh1VluRuXbfGgDt4HVVlQZl0coUs1qMH'
	ACCESS_SECRET = 'caNU6qujBBWJhDsiwGqw5QtWxCv4tI2OqU0TvjF2SorV4'

	TweetBot = twitter_setup(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

	if str(chat_id) in AUTHCHATS:

		if content_type == 'text':
			if msg['text'] == '/menú' or msg['text'] =='/start':
				bot.sendMessage(chat_id, 'Menú de opciones programadas: \n/twit para twittear\n/greet para twittear saludo al azar'
				'\n/retwittear para postear según palabra clave\n/imagen para twittear imagen\n/menciones para ver Tweets donde he sido mencionado'
				'\n/feed para ver notificaciones\n/seguidores para ver listado de los últimos seguidores')

			# Hacer un Tweet
			if msg['text']=='/twit':
				bot.sendMessage(chat_id, "Escribir Twit:")
				TWEETWHAITHING.append(chat_id)
			elif chat_id in TWEETWHAITHING:
				try:
					TweetBot.update_status(msg['text'])
					bot.sendMessage(chat_id, 'Tweet enviado')
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)
				TWEETWHAITHING.remove(chat_id)

			# Tweetear saludo al azar
			if msg['text']=='/greet':
				try:
					mensajes = ["Hola desde Python","Hello","Salut/Bonjour!","Hallo","Guten Tag","Ciao!","Olá","привет","Namaste","Aloha!","Konnichi wa","Ni Hao!",]
					rand = random.choice(mensajes)
					TweetBot.update_status(rand)
					bot.sendMessage(chat_id, 'Saludo al azar Tweeteado')
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)

			# Retweet segun palabra clave
			if msg['text']=='/retwittear':
				bot.sendMessage(chat_id, "Palabra clave:")
				TWEETWHAITHING.append(chat_id)
				numberofTweets = 1
				for tweet in tweepy.Cursor(api.search, q=msg['text']).items(numberofTweets):
					try:
						tweet.retweet()
					except tweepy.TweepError as e:
						print(e.reason)
					finally:
						bot.sendMessage(chat_id,"Retweeteado!")
						TWEETWHAITHING.remove(chat_id)

			# Postear una imagen
			if msg['text']=='/imagen':
				bot.sendMessage(chat_id, "Subiendo....")
				TWEETWHAITHING.append(chat_id)
			elif chat_id in TWEETWHAITHING:
				try:
					mensajes = ["Hola desde Python","Hello","Salut/Bonjour!","Hallo","Guten Tag","Ciao!","Olá",
					"привет","Namaste","Aloha!","Konnichi wa","Ni Hao!",]
					rand = random.choice(mensajes)
					file ='D:/Documentos/Python/Seminario de Software/my_bot/images/wp2.jpg'
					with open('D:/Documentos/Python/Seminario de Software/my_bot/images/wp2.jpg', 'rb') as photo:
						TweetBot.update_with_media(media=photo, status=rand, filename=file)
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)
				finally:
					bot.sendMessage(chat_id, "Subida con éxito!")

			# Menciones
			if msg['text']=='/menciones':
				try:
					menciones = api.mentions_timeline()
					for mencion in menciones:
						bot.sendMessage(chat_id, str(mencion.id) + ' - ' + mencion.text)
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)

			# Feed
			if msg['text']=='/feed':
				try:
					public_tweets = api.home_timeline(count=5)
					for tweet in public_tweets:
						bot.sendMessage(chat_id,tweet.text)
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)

			# Seguidores
			if msg['text']=='/seguidores':
				try:
				    seguidores = api.followers()
				    for follower in seguidores:
				        bot.sendMessage(chat_id,follower.screen_name)
				except tweepy.TweepError as e:
					bot.sendMessage(chat_id, e.reason)


	else: # Acceso al chat
		if chat_id in AUTHWHAITING:
			if msg['text'] == AUTHCODE:
				bot.sendMessage(chat_id, "Autorizacion Correcta, Ingrese su Nombre, Correo y Numero celular Separado por comas")
				AUTHDATA.append(chat_id)
			else:
				bot.sendMessage(chat_id,"Codigo incorrecto")

			AUTHWHAITING.remove(chat_id)
		elif chat_id in AUTHDATA:
			data = msg['text'].replace(", ", ",")
			userData = data.split(",")

			userData[2]= userData[2].replace("-", "")
			userData[2]= userData[2].replace(" ", "")
			if len(userData) == 3:
				if((validate_email(userData[1])) and (userData[2][0] in ['3','8','9'] and len(userData[2])==8)):
					bot.sendMessage(chat_id,"Usuario autorizado exitosamente.")
					AUTHDATA.remove(chat_id)
					AUTHCHATS[str(chat_id)] = [userData[0], userData[1], userData[2],userData[3],userData[4],userData[5],userData[6]]
					with open('authchats.txt', 'a') as f:
						f.write(str(chat_id) + "," + userData[0] + "," + userData[1] + "," + userData[2]+ "\n")

				else:
					bot.sendMessage(chat_id,"Correo o Numero de celular invalido. Ingrese su Nombre, Correo y Numero celular Separado por comas")
			else:
				bot.sendMessage(chat_id,"Datos Incorrecto. Ingrese su Nombre, Correo y Numero celular Separado por comas")
		else:
			if msg['text'] == "/autorizar":
				bot.sendMessage(chat_id, "Ingrese el codigo de autorizacion")
				AUTHWHAITING.append(chat_id)
			else:
				bot.sendMessage(chat_id, "Usuario No Autorizado, utilice el comando /autorizar")



with open('authchats.txt') as f:
	for linea in f:
		dataLinea = linea.split(",")
		AUTHCHATS[dataLinea[0]] = [dataLinea[1], dataLinea[2], dataLinea[3]]


with open('auttweets.txt') as f:
	for linea in f:
		dataLinea = linea.split(",")
		AUTHCHATS[dataLinea[0]] = [dataLinea[1], dataLinea[2], dataLinea[3],dataLinea[4]]


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

def twitter_setup(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api

def get_tweet(tweet):
	bot.sendMessage(chat_id,"Tweet Message : " + tweet.text)
	bot.sendMessage(chat_id, "Tweet Favorited \t:" + str(tweet.favorited))
	bot.sendMessage(chat_id,"Tweet Favorited count \t:" + str(tweet.favorite_count))

	if hasattr(tweet, 'retweeted_status'):
		bot.sendMessage(chat_id, "Tweet send by : " + tweet.retweeted_status.user.screen_name)
		bot.sendMessage(chat_id, "Original tweet ID" + tweet.retweeted_status.id_str)

		for screenname in tweet.retweeted_status.entities['user_mentions']:
			bot.sendMessage(chat_id, "Mention user: " + str(screenname['screen_name']))

while 1:
	time.sleep(5)
