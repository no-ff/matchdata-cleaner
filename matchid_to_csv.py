import requests
from riotwatcher import LolWatcher, ApiError

input = []

def convert(match_ids: list[str], api_key: str) -> str:
    for match in match_ids:
        match_info = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" %(match, api_key)).json()
        if "info" in match_info:
            game_length = (match_info["info"])["gameDuration"]
            Total += game_length