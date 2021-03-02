import os
import requests
import json
from dotenv import load_dotenv






load_dotenv()
global KEY 
#Get RIOT-API key from .env file
KEY = os.getenv('RIOT_API')

#Encrypted ID is required for most of the API calls
def getEncryptedID(summonerName):
    url="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}"
    url = url.format(summonerName, KEY)
        
    response = requests.get(url)
    id = response.json()['id']

    return id

#in progress
def getCurrentGameInfo(summonerName):
    id = getEncryptedID(summonerName)

    url="https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{}?api_key={}"
    url = url.format(id, KEY)

    response = requests.get(url).json()
    jprint(response)
    elapsed_time = (response['gameLength'] / 60)
    match = ("The game has been running for {} minutes").format(elapsed_time)
    return match

def getPlayerInfo(summonerName):
    id = getEncryptedID(summonerName)

    url="https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}"
    url = url.format(id, KEY)

    response = requests.get(url).json()
    print(response)
    #jprint(response.json())

    rank = response[0]['rank']
    tier = response[0]['tier']
    win = response[0]['wins']
    lose = response[0]['losses']

    info="Player {} is {} {} with {} wins and {} losses... What a noob :DDD"
    info= info.format(summonerName, tier, rank, win, lose)
    return info


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
