import requests
from bs4 import BeautifulSoup
import pandas as pd

def getTopPlayers():
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

# print(getTopPlayers())