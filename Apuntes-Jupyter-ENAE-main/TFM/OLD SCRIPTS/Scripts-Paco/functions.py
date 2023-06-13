from riotwatcher import LolWatcher, ApiError
import requests
import pandas as pd

def getMatches():
    apikey = "RGAPI-91035564-476d-4697-a7ae-11f5c0258945"

    api_key = apikey
    api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/GayolaVirtual"


    api_url = api_url + '?api_key=' + api_key
    resp = requests.get(api_url)
    player_info = resp.json()

    player_account_id = player_info['accountId']
    puuid= player_info['puuid']

    api_key = apikey
    api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/axJpeMVpuqmZmkqA-2A94bZJQ4KsZJLUzeIGhFmYGUJT5vs7Ewpad4RidtrBlmdT9B_DrALIZDp5qQ/ids?start=0&count=20"


    api_url = api_url + "&api_key="  + api_key

    resp = requests.get(api_url)
    matches = resp.json()

    for i in matches:
        if i == "EUW1_6344380455":  # ponerlo nomral para que saque las 20 partidas
            api_url =f"https://europe.api.riotgames.com/lol/match/v5/matches/{i}"
            api_url = api_url+ "?api_key=" +api_key
        
            resp = requests.get(api_url)
        
            matchInfo = resp.json()
        
            # print (matchInfo)
        
            part_index  =  matchInfo['metadata']['participants'].index(puuid)
        
            Champion    = matchInfo['info']['participants'][part_index]['championName'] 
            Kilss       = matchInfo['info']['participants'][part_index]['championId'] 
            Deaths      = matchInfo['info']['participants'][part_index]['deaths'] 
            Assistans   = matchInfo['info']['participants'][part_index]['assists']
            GameModo    = matchInfo['info']['gameMode']
            GameDuration= matchInfo['info']['gameDuration']
        
            #print(f"Champion: {Champion}        kills: {Kilss}      Deaths: {Deaths}        Assists: {Assistans}        Modo de juego: {GameModo}       duración del juego: {GameDuration}")
    return matchInfo

# print(getMatches())