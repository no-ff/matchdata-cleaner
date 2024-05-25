import requests
import time


def player_to_match_ids(puuid: str, api_key: str, amount: int, start: int) -> list[str]:
    # Get last x games of the player.
    # Start: starting at x recent game going down.
    # Ranked games only.
    req = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids?queue=420&start=%i&count=%i&api_key=%s" % (
        puuid, start, amount, api_key)
    matches = requests.get(req)
    if matches.status_code == 429:
        print("Rate Limit Exceeded, gonna sleep a bit")
        time.sleep(120)
        matches = requests.get(req)
    matches = matches.json()
    return matches


def matchId_to_match(match_id: str, api_key: str) -> dict:
    # Returns the match data from match_id.
    req = "https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" % (
        match_id, api_key)
    match = requests.get(req)
    if match.status_code == 429:
        print("Rate Limit Exceeded, gonna sleep a bit")
        time.sleep(120)
        match = requests.get(req)
    match = match.json()
    return match


def bfs_get_match_ids(amount: int, start: str, already: dict[str, int], api_key: str):
    # Get recent x games of the start player.
    # Start: matchID.
    # Go through each of them, save the match_ids. (Checks whether it already is in 'already')
    # Then add the players of each game into the queue.
    # Repeat until target amount has been met.
    f = open("matchids.txt", "a")

    counter = 0
    ret_matches = []
    queue = [start]
    while (queue is not None) and counter < amount:
        # Convert matchid to match datatype
        matchType = matchId_to_match(queue[0], api_key)
        puuids = matchType["metadata"]["participants"] # Grab all 10 players to initially fill up the queue.
        for player in puuids:
            # Get last matches of players.
            # Idea: Check the player's specific rank. (Unfortunately not available in API)
            new_matches = player_to_match_ids(player, api_key, 50, 0)
            for match in new_matches:
                in_already = already.get(match, 0)
                if in_already == 0:
                    already[match] = 1
                    queue.append(match)
                    ret_matches.append(match)
                    f.write(match+ "\n")
        queue.pop(0)

    f.close()
    return ret_matches


"""
if __name__ == "__main__":
    api_key = ""
    start = ""
    print(bfs_get_match_ids(1, start, [start]))
"""
