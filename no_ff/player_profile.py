import requests
import json
def get_puuid(name, tagline, key):
    puuid_data = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tagline}?api_key={key}")
    # need to check errors
    puuid_data = puuid_data.json()
    puuid = puuid_data['puuid']
    return puuid

def get_matches(puuid, key, count):
    match_data = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={key}")
    # need to check errors
    match_data = match_data.json()
    return match_data

def get_match_data(match_id, key):
    match_data = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={key}")
    # need to check errors
    match_data = match_data.json()
    return

def get_player_data(player_json):
    """For each player, need sums, items, kda, cs (cs per m), runes, rank, champ, wards damage, player name, """
    player_data = {}
    player_data['username'] = player_json['summonerName']
    player_data['champion'] = player_json['championName']
    player_data['kda'] = f"{player_json['kills']}/{player_json['deaths']}/{player_json['assists']}"
    player_data['cs'] = player_json['totalMinionsKilled']
    player_data['cs_per_min'] = player_json['goldEarned'] / player_json['gameDuration']
    player_data['wards'] = player_json['wardsPlaced']
    player_data['damage'] = player_json['totalDamageDealtToChampions']
    player_data['damageTaken'] = player_json['totalDamageTaken']
    player_data['items'] = [player_json['item0'], player_json['item1'], player_json['item2'], player_json['item3'], player_json['item4'], player_json['item5'], player_json['item6']]
    player_data['runes'] = player_json['perks']

def decoding_runes(runes):
    runeFile = open("runesReforged.json", "r")
    runeFile = json.load(runeFile)
    runesDir = {}
    for runes in runeFile:
        key = runes['id']
        runesDir[runes['id']] = runes['key']
        for category in runes['slots']:
            for rune in category['runes']:
                runesDir[rune['id']] = rune['name']
    print(runesDir)
    outputRunes = open("runes.json", "w")
    outputRunes.write(json.dumps(runesDir))


if __name__ == "__main__":
    