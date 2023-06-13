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

# Accedemos al diccionario del nombre en concreto del usuario, si no existe en esa region, que nos de error:
try:
    summoner = watcher.summoner.by_name(region, summoner_name)  # comporbar dir(summoner)
except ApiError as err:
    if err.response.status_code == 404:
        print('El invocador no existe en la región especificada.')
    else:
        raise

# Obtenemos los IDs de las últimas 20 partidas del invocador
try:
    matchlist = watcher.match.matchlist_by_puuid(region, summoner['puuid'], count=20)
except ApiError as err:
    if err.response.status_code == 404:
        print('No se encontraron partidas para el invocador especificado.')
    else:
        raise

# print(matchlist)

# Obtener los detalles de cada partida por su ID
matches = []

for idMatch in matchlist: 
    match_detail = watcher.match.by_id(region,idMatch) 
    matches.append(match_detail)
 
# Imprimir los detalles de cada partida
#for match_detail in matches:
#    print(match_detail)