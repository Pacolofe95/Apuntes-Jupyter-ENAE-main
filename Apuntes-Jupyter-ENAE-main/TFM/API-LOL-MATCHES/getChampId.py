import requests
import pandas as pd

def getChampionsId():
    url = "http://ddragon.leagueoflegends.com/cdn/13.6.1/data/en_US/champion.json"
    page = requests.get(url)
    page.status_code # vemos que es 200, no hace falta cambiar el userAgent
    
    if page.status_code == 200:
         dictCompleto = page.json()
    else:
         print(f"Error al descargar el JSON: {page.status_code}")
         
    
    dictCampeones = dictCompleto["data"]
    clavesCampeones = list(dictCampeones.keys())
    clavesCampeonesFinal = list()
    
    for a in clavesCampeones:
        valores = a.lower()
        
        if valores == "monkeyking":
            valores = "wukong"
        
        clavesCampeonesFinal.append(valores)
        
    
    idCampeon = list()
   
    for clave in clavesCampeones:
        idCampeon.append(dictCampeones[clave]["key"])
    
    dfIdChampions = pd.DataFrame({"ID" : idCampeon ,"Champion" : clavesCampeonesFinal})    
    return dfIdChampions 

dfIdChampions = getChampionsId()

# exportamos a csv 
#dfIdChampions.to_csv('C:/Users/gonza/OneDrive/Escritorio/TFM/Python/outputs/dfIdChampions.csv', index=False)