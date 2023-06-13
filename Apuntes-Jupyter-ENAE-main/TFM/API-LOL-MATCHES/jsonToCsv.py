
"""
Script para la extarcción de los archivos json de la capa bronze, conversion a csv con todas su columnas 
y posterior carga a la capa silver con la misma organizacion en carpetas.
"""
import pandas as pd
import json


# Cargar el archivo JSON

partida = json.load(open("EUW1_6416045145.json"))

#######
# prueba = pd.read_json("EUW1_6416045145.json") # esto crea un df de 2 columnas con los dos elementos principales dle json
#######

# CONVERTIMOS EN DF EL JSON - TODO EN UNA UNICA FILA (LOS SUBDICCIONARIOS SIGUEN SIN SEPARAR)

dfPartida = pd.json_normalize(partida)

# metadata = partida["metadata"]
# info     = partida["info"] 

for fila in dfPartida.iterrows():
    for elemento in dfPartida["info.participants"]:
            df2 = pd.DataFrame(elemento)
df2.to_csv("csvPart1.csv")
df3 = dfPartida#.drop(columns=['metadata.participants','info.teams','info.participants','info.tournamentCode'])


df3q = df3.loc[df3.index.repeat(10)]
df3q.to_csv("csvPart2.csv")

df1 = pd.read_csv('csvPart2.csv')
df2 = pd.read_csv('csvPart1.csv')

df_concatenated = pd.concat([df1, df2], axis=1)
#df_concatenated.to_csv("Final.csv", index=False)

###### LOGICA EXTRACCION DE SUBDICCIONARIOS 

listconcatenated = df_concatenated["info.participants"].to_json()

JSONlistaconcatenated = json.loads(listconcatenated)

for a in JSONlistaconcatenated:
    for b in a:
     cadena_info_participants = JSONlistaconcatenated[b]

lista_diccionarios = eval(cadena_info_participants)

df_info_participants = pd.DataFrame(lista_diccionarios)

##### PARA CHALLENGES DENTRO DE INFO PARTICIPANTS

listconcatenated2 = df_info_participants["challenges"].to_json()

JSONlistaconcatenated2 = json.loads(listconcatenated2)

dfa = pd.DataFrame()
for a in JSONlistaconcatenated2:
    for b in a:
     cadena_info_participants_challenges = JSONlistaconcatenated2[b]
     staging = pd.json_normalize(cadena_info_participants_challenges)
     dfa = dfa.append(staging, ignore_index= True)

#lista_diccionarios2 = eval(cadena_info_participants_challenges)

#df_info_participants_challenges = pd.json_normalize(cadena_info_participants_challenges)

