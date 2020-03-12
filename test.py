import sys
import time
import telepot
from telepot.loop import MessageLoop
from validate_email import validate_email
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# import menu
# from data import *

AUTHCHATS = {}
TOKEN = "894152792:AAF9F8dQwkLiGxdmbtRqCTC_Q1xHg7WE1pI"
bot = telepot.Bot(TOKEN)

AUTHCODE = "Unicah123"

AUTHWHAITING = []
AUTHDATA = []


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	#print(content_type, chat_type, chat_id)

	if str(chat_id) in AUTHCHATS:
		if content_type == 'text':
			#accion del Bot
			bot.sendMessage(chat_id, msg['text'])

	else: #Proceso de Autorizacion al chat.
		if chat_id in AUTHWHAITING:
			if msg['text'] == AUTHCODE:
				bot.sendMessage(chat_id, "Autorizacion Correcta, Ingrese su Nombre, correo y celular separado por comas.")
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
					AUTHCHATS[str(chat_id)] = [userData[0], userData[1], userData[2]]
					with open('authchats.txt', 'a') as f:
						f.write(str(chat_id) + "," + userData[0] + "," + userData[1] + "," + userData[2] + "\n")

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


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
while 1:
    time.sleep(10)
