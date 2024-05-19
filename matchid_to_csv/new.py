import requests

api_key = "RGAPI-4ffbc243-e506-4653-9f9c-1fc10db5c39e"
match = "NA1_5000912851"
match_info = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" %(match, api_key))
match_info = match_info.json()
print(match_info['info']['participants'])