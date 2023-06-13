import pandas as pd
from azure.storage.blob import BlobServiceClient
from variables import STRING
from funcionesModelos import kdaWinLoseEngine
import csv
import io



# Configurar los valores de las variables
connection_string = STRING
capa_plata = "silver-layer"
capa_oro   = "gold-layer"

# Crear el cliente del servicio Blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Obtener el contenedor de origen
container_client = blob_service_client.get_container_client(capa_plata)

# Obtener la lista de blobs en el contenedor de origen
blobs = container_client.list_blobs()

dfGeneral = pd.DataFrame()

for blob in blobs:
    count = 0
    blob_client = container_client.get_blob_client(blob)
    stream = blob_client.download_blob().readall().decode('utf-8')
    df = pd.read_csv(io.StringIO(stream))
       
    for modo in df["info.gameMode"]:
        if modo == "CLASSIC":
            count = count +1
    
    if count > 0:
        dfWinLose = kdaWinLoseEngine(df)
        dfGeneral = pd.concat([dfGeneral, dfWinLose], ignore_index= True)
        dfGeneral = dfGeneral.reset_index(drop = True)

dfGeneral.drop(columns=["info.gameMode_x", "info.gameMode_y"], inplace = True)
output_container_client = blob_service_client.get_container_client(capa_oro)
blob_name = "Mod2KdaWinLose.csv"
blob_client = output_container_client.get_blob_client(blob_name)
blob_client.upload_blob(dfGeneral.to_csv(index=False), overwrite=True)