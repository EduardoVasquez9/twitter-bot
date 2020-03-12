import tweepy
import os
import time
import random
from data import *

# limpiar pantalla
clear = lambda: os.system('cls')
clear()

print("\n\nI N S T R U C C I O N E S\n")
print("1. Twittear")
print("2. Twittear saludo al azar")
print("3. Retweet según palabra clave")
print("4. Twittear de @WhatTheFFacts")
print("5. Twittear imagen")
print("6. Ver últimos Tweets del feed")
print("7. Notificaciones/Menciones")
print("8. Follow a todos los que me siguen")
print("9. Salir\n")

opc = int(input("Ingrese el número de su selección: "))
if opc == 1:
    tweet = str(input("Tweet: "))
    api.update_status(tweet)
elif opc == 2:
    import tweet
elif opc == 3:
    import retweet
elif opc == 4:
    # import facts
    print("Faltan correcciones")
elif opc == 5:
    print("Pendiente")
elif opc == 6:
    clear()
    # ver ultimos 20 Tweets
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
elif opc == 7:
    clear()
    print("Menciones/Notificaciones\n")
    menciones = api.mentions_timeline()
    for mencion in menciones:
        print(str(mencion.id) + ' - ' + mencion.text)
elif opc == 8:
    # seguir a todos los que siguen la cuenta
    user = api.me()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Se dió Follow a todos los que siguen a " + user.name)
elif opc == 9:
    print("\nSaliendo...")
    raise SystemExit
