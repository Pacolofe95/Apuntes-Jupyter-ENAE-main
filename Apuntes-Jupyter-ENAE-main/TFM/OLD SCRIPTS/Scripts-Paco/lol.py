from riotwatcher import LolWatcher, ApiError
import requests
import pandas as pd


api_key = 'RGAPI-91035564-476d-4697-a7ae-11f5c0258945'
api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Noah7"


api_url = api_url + '?api_key=' + api_key
resp = requests.get(api_url)
player_info = resp.json()

player_account_id = player_info['accountId']


api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/axJpeMVpuqmZmkqA-2A94bZJQ4KsZJLUzeIGhFmYGUJT5vs7Ewpad4RidtrBlmdT9B_DrALIZDp5qQ/ids?start=0&count=20"
api_url = api_url + "&api_key=" +api_key
resp = requests.get(api_url)

match = resp.json()
print(match)

api_url ="https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_6246974414"
api_url = api_url+ "?api_key=" +api_key

resp = requests.get(api_url)

matchInfo = resp.json() 
metadata_info = matchInfo['metadata'].keys()
print(metadata_info)
# print("----------------------------------------------------------")
# print(matchInfo['info'])
# print("----------------------------------------------------------")
# print(matchInfo['metadata'])
# print("----------------------------------------------------------")


data_info = matchInfo['info'].keys()
puuid =  player_info['puuid']

part_index =  matchInfo['metadata']['participants'].index(puuid)
print(matchInfo['info']['participants'][part_index]['championName'])







