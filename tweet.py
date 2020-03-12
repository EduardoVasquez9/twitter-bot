import os
import time
import random
from data import *

mensajes = ["Hola desde Python","Hello","Salut/Bonjour!","Hallo","Guten Tag","Ciao!","Olá",
            "привет","Namaste","Aloha!","Konnichi wa","Ni Hao!",]
rand = random.choice(mensajes)
# This will update our timeline
api.update_status(rand)
