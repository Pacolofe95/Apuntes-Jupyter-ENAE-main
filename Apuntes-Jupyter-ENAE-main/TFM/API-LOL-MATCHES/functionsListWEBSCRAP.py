import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
from azure.storage.blob import BlobServiceClient



def getTopPlayers() -> list:
    """
    Sacamos el top 500 jugadores de Europa a traves de league of graphs haciendo web scrapping con beautifulsoup.
    """
    userAgent = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    listaNombres = list()

    for j in range (1,6):
        if j==1:
            url = 'https://www.leagueofgraphs.com/es/rankings/summoners/euw'
            req = requests.get(url, headers = userAgent)
            soup = BeautifulSoup(req.text, "html.parser")

            nombres = soup.find_all("span", class_ = "name")

            for i in range (len(nombres)):
                listaNombres.append(nombres[i].text)
        if j > 1:
            url = 'https://www.leagueofgraphs.com/es/rankings/summoners/euw/page-' + str(j)
            req = requests.get(url, headers = userAgent)
            soup = BeautifulSoup(req.text, "html.parser")

            nombres = soup.find_all("span", class_ = "name")

            for i in range (len(nombres)):
                listaNombres.append(nombres[i].text)


    return listaNombres

def getChampionRole() -> pd.DataFrame:
    """
    Nos saca un dataset con todos los campeones del juego y su role.
    """

    url         = "https://www.leagueofgraphs.com/champions/counters/euw/master"
    userAgent   = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    page = requests.get(url, headers = userAgent)
    soup = BeautifulSoup(page.text, "html.parser")

    stage        = list()
    championsDef = list()

    names = soup.find_all("div", class_ = "img-align-block block-medium-up width-62-on-small")

    for i in range(len(names)):
       stage.append(names[i].text)
       sinEspacios = stage[i].strip().replace("\n" , "").replace("                      ", " ").replace("'","").replace(".", "").lower()
       championsDef.append(sinEspacios)

    df = pd.DataFrame({"Champion-Role" : championsDef})
    df[["Champion" , "Role"]] = df["Champion-Role"].str.split("  ", expand = True)
    ChampionRole = df.drop("Champion-Role", axis = 1 )

    columnaSus = list()
    for nombre in ChampionRole["Champion"]:
        nombreSus = nombre.replace(" ", "")
        if nombreSus == "nunu&willump":
            nombreSus = "nunu"
        if nombreSus == "renataglasc":
            nombreSus = "renata"
        columnaSus.append(nombreSus)

    ChampionRole["Champion"] = columnaSus

    return ChampionRole

def getChampionsId() -> pd.DataFrame:
    """
    Obtenemos un dataset con el nombre de los campeones y su id en la api de riot.
    """
    url  = "http://ddragon.leagueoflegends.com/cdn/13.6.1/data/en_US/champion.json"
    page = requests.get(url)
    page.status_code # vemos que es 200, no hace falta cambiar el userAgent

    if page.status_code == 200:
         dictCompleto = page.json()
    else:
         print(f"Error al descargar el JSON: {page.status_code}")


    dictCampeones        = dictCompleto["data"]
    clavesCampeones      = list(dictCampeones.keys())
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

# Comporbacion nombres e id (join)
# antijoin = pd.merge(dfChampionRole, dfIdChampions, left_on='Champion', right_on='Champion', how='outer', indicator=True)

