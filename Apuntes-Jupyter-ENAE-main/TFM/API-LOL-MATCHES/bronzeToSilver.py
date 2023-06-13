import pandas as pd
import os
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from functionsListDATALAKE import normalize_json
from variables import STRING

# Configurar los valores de las variables
connection_string = STRING
capa_bronce = "bronze-layer"
capa_plata = "silver-layer"

# Crear el cliente del servicio Blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Obtener el contenedor de origen
container_client = blob_service_client.get_container_client(capa_bronce)

# Obtener la lista de blobs en el contenedor de origen
blobs = container_client.list_blobs()

# Procesar cada blob y guardar el CSV resultante en el contenedor de destino
for blob in blobs:
    # Comprobar si el blob ya existe en el contenedor silver-layer
    if blob.name[:-5] + ".csv" not in capa_plata:                      # El "[:-5]" es para quitar el ".json"
        blob_client = container_client.get_blob_client(blob)
        blob_data = json.loads(blob_client.download_blob().content_as_text())
        
        df = normalize_json(blob_data)
        
        for fila in df.iterrows():
            for elemento in df["info.participants"]:
                    df2 = pd.DataFrame(elemento)
        df2.to_csv("csvPart1.csv")
        df3 = df.drop(columns=['metadata.participants','info.teams','info.participants','info.tournamentCode'])


        df3q = df3.loc[df3.index.repeat(10)]
        df3q.to_csv("csvPart2.csv")

        df1 = pd.read_csv('csvPart2.csv')
        df2 = pd.read_csv('csvPart1.csv')

        df_concatenated = pd.concat([df1, df2], axis=1)
        df_concatenated.to_csv("Final.csv", index=False)
        
        # Escribir los resultados en un archivo CSV en el contenedor de destino
        output_container_client = blob_service_client.get_container_client(capa_plata)
        blob_name = os.path.splitext(blob.name)[0] + ".csv"
        blob_client = output_container_client.get_blob_client(blob_name)
        blob_client.upload_blob(df_concatenated.to_csv(index=False), overwrite=True)