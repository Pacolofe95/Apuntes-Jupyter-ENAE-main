import json
import pandas as pd
from azure.storage.blob import BlobServiceClient
from variables import STRING

def normalize_json(data):
    if isinstance(data, dict):
        
        return pd.json_normalize(
            data,
            record_path=None,
            meta=None,
            meta_prefix=None,
            record_prefix=None,
            errors='raise',
            sep='.',
            max_level=None
        )
    elif isinstance(data, list):
        
        return pd.concat([normalize_json(item) for item in data], ignore_index=True)
    else:
        
        return data


# with open('jsonLol.json') as f:
#     datos = json.load(f)


# df = normalize_json(datos)
# df3 = df


# for fila in df.iterrows():
#     for elemento in df["info.participants"]:
#             df2 = pd.DataFrame(elemento)
# df2.to_csv("csvPart1.csv")
# df3 = df3.drop(columns=['metadata.participants','info.teams','info.participants','info.tournamentCode'])


# df3q = df3.loc[df3.index.repeat(10)]
# df3q.to_csv("csvPart2.csv")

# df1 = pd.read_csv('csvPart2.csv')
# df2 = pd.read_csv('csvPart1.csv')

# df_concatenated = pd.concat([df1, df2], axis=1)
# df_concatenated.to_csv("Final.csv", index=False)

def getJSONfromBronze() -> list:
    """
    Comprobacion del listado de archivos JSON en nuestro BlobStorage en la capa Bronze
    """
    connection_string   = STRING

    # Crear contenedor si aún no existe
    container_name   = "bronze-layer"
    container_client = blob_service_client.get_container_client(container_name)

    bloblist = container_client.list_blobs()

    listado = []
    for blob in bloblist:
        listado.append(blob['name'])

    return listado

                         
                

            
