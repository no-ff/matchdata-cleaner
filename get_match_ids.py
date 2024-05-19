import requests
import time
from matchid_to_csv import convert

def player_to_match_ids(puuid:str, api_key:str, amount: int, start: int) -> list[str]:
    #get last x games of the player
    # start: starting at x recent game going down
    req = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids?start=%i&count=%i&api_key=%s" %(puuid, start, amount, api_key)
    matches = requests.get(req)
    if matches.status_code == 429:
        print("Rate Limit Exceeded, gonna sleep a bit")
        time.sleep(20)
        matches = requests.get(req)
    matches = matches.json()
    return matches

def matchId_to_match(match_id:str, api_key:str) -> dict:
    #returns the match data from match_id
    req = "https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" %(match_id, api_key)
    match = requests.get(req)
    if match.status_code == 429:
        print("Rate Limit Exceeded, gonna sleep a bit")
        time.sleep(20)
        match = requests.get(req)
    match = match.json()
    return match

def bfs_get_match_ids(amount: int, start: str, already: list[str], api_key: str, file_name: str):
    
    #get recent x games of the start player
    #start: matchID
    #go through each of them , save the match_ids. (checks whether it already is in 'already')
    #then add the players of each game into the queue
    
    #repeat until target amount has been met
    counter = 0
    ret_matches = []
    queue = [start]
    start_time = time.time()
    while (queue is not None) and counter < amount:
        #need to convert matchid to match datatype
        matchType = matchId_to_match(queue[0], api_key)
        iteration_first = time.time()
        print(f"iteration first time, {iteration_first - start_time}")
        convert(matchType, api_key, file_name, queue[0])
        iteration_second = time.time()
        print(f"iteration second time, {iteration_second - start_time}")
        puuids = matchType["metadata"]["participants"]
        for player in puuids:
            #get last matches of players
            new_matches = player_to_match_ids(player, api_key, 5, 0)

            for match in new_matches:
                #if match not in already:
                queue.append(match)
                already.append(match)
                ret_matches.append(match)

        queue.pop(0)
        counter += 1




"""
if __name__ == "__main__":
    api_key = ""
    start = ""
    print(bfs_get_match_ids(1, start, [start]))
"""