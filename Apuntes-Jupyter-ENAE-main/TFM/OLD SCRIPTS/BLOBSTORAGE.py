# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:37:10 2023

@author: gonza
"""

import pandas as pd
import pyodbc
from azure.storage.blob import BlobServiceClient
import json

from functions import getMatches

connection_string = "DefaultEndpointsProtocol=https;AccountName=enaedatalake;AccountKey=y/MmOtIFs/YeAr0YO91DpAsuijr3J9ALHVl1kgDSieJKAxY48pRISzPUWGQoTeZec6k3LsZ5A0x0+ASt9/25wQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Crear contenedor si aún no existe
container_name = "api-lol"
container_client = blob_service_client.get_container_client(container_name)

if not container_client.exists():
    container_client.create_container()
    

matches = getMatches()
print(matches)
blob_name = "matches.json"
# json_data = {"name": "John", "age": 30}
# blob_name = "<nombre_del_blob>.json"
# Serializar objeto JSON a una cadena y cargarlo en el blob
blob_client = container_client.get_blob_client(blob_name)
json_string = json.dumps(matches)
blob_client.upload_blob(json_string, overwrite=True)