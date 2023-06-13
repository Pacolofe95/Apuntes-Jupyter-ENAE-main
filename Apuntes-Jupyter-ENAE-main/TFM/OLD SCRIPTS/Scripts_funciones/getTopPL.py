import requests
from bs4 import BeautifulSoup
import pandas as pd

userAgent = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

listaNombres = list()
listaPL = list()

for j in range (1,6):
    if j==1:
        url = 'https://www.leagueofgraphs.com/rankings/summoners/euw'
        req = requests.get(url, headers = userAgent)
        soup = BeautifulSoup(req.text, "html.parser")

        nombres = soup.find_all("span", class_ = "name")
        for i in range (len(nombres)):
            listaNombres.append(nombres[i].text)
            
        puntos = soup.find_all('td', class_="text-center")
        for punto in puntos:
            if len(punto['class']) == 1:
                listaPL.append(punto.find('div', class_="summonerTier").text.strip().replace(" "*40, "").replace("\n", " "))
    if j > 1: 
        url = 'https://www.leagueofgraphs.com/rankings/summoners/euw/page-' + str(j)
        req = requests.get(url, headers = userAgent)
        soup = BeautifulSoup(req.text, "html.parser")

        nombres = soup.find_all("span", class_ = "name")
        for i in range (len(nombres)):
            listaNombres.append(nombres[i].text)
            
        puntos = soup.find_all('td', class_="text-center")
        for punto in puntos:
            if len(punto['class']) == 1:
                listaPL.append(punto.find('div', class_="summonerTier").text.strip().replace(" "*40, "").replace("\n", " "))
                
dimRanking = pd.DataFrame({"Usuario": listaNombres, "ELO-PL": listaPL})

#print (dimRanking)

# dimRanking.to_csv('C:/Users/Fernando/Documents/DANIEL/Daniel_UM/ENAE/TFM/Apuntes-Jupyter-ENAE/TFM/dimRanking.csv', index=False)