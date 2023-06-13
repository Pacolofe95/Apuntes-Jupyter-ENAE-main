from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
import os, json
import pandas as pd
from functionsListWEBSCRAP import getTopPlayers
from functionsListDATALAKE import getJSONfromBronze
from azure.storage.blob import BlobServiceClient
import json
import datetime
from variables import API_KEY, STRING

#################CONEXION BLOBSTORAGE########################
connection_string = STRING
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Crear contenedor si aún no existe
container_name = "bronze-layer"
container_client = blob_service_client.get_container_client(container_name)

if not container_client.exists():
    container_client.create_container()
    
#############################################################


######################PREPARAMOS ENTORNO API#################
api_key = API_KEY
watcher = LolWatcher(api_key)
region = 'EUW1'
############################################################


## CARGO EL LISTADO DE JSON EN LA CAPA BRONZE Y QUITO EL .json ##
listJSONBronze  = getJSONfromBronze()
listanombrefinal = []

for a in listJSONBronze:
    sinFecha = a.split("/")[1]
    sinExtension = sinFecha.split(".")[0]
    listanombrefinal.append(sinExtension)
    
## OBTENGO LA LISTA CON EL TOP500 ##
summoner_name   = getTopPlayers() # aqui debemos de poner la lista con el top500
nameList        = []
allMatches      = []

for nombre in summoner_name:
    try:
        #nameList.append(nombre)
        
        summoner  = watcher.summoner.by_name(region, nombre)
        matchlist = watcher.match.matchlist_by_puuid(region, summoner['puuid'], count=1)
        allMatches.append(matchlist)
    except:
        print("Se produjo un error")
        print(nombre)
        continue

dfMatchesID     = pd.DataFrame(allMatches)
dfMatchesID     = dfMatchesID.drop_duplicates()
matchesIdFinal  = dfMatchesID[0].tolist()  #LISTA SIN DUPLICADOS

for idMatch in matchesIdFinal:
        if f"{idMatch}" in listanombrefinal:
            print(f'Ya existe{idMatch}')
        else:
            match_detail = watcher.match.by_id(region,idMatch) 
            #matches.append(match_detail)
            blob_name   = str(datetime.date.today().strftime("%d-%m-%Y")) +"/" + idMatch + ".json"
            blob_client = container_client.get_blob_client(blob_name)
            json_string = json.dumps(match_detail)
            blob_client.upload_blob(json_string, overwrite=True) 