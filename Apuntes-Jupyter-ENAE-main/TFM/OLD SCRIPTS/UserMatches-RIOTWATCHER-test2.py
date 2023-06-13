from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
import os, json
import pandas as pd

# Preparamos el entorno: clave API, región y nombre usuario
api_key = "RGAPI-8b9b4104-b098-41a0-aa5e-1b8b298917a5"
watcher = LolWatcher(api_key)
region = 'EUW1'
summoner_name = 'Noah7' # aqui debemos de poner la lista con el top500

# PARA VER QUE FUNCIONES CONTIENE WATCHER: dir(watcher)

# Accedemos al diccionario del nombre en concreto del usuario

summoner = watcher.summoner.by_name(region, summoner_name)  # comporbar dir(summoner)

# Obtenemos los IDs de las últimas 20 partidas del invocador

matchlist = watcher.match.matchlist_by_puuid(region, summoner['puuid'], count=20)

print(matchlist)