import requests
import json

puuid = '_numZ7P_3tZlzeC8lkHSBsY5MIKVje1kvHNJlt7_Wp9fKEhwJss6VMAc0HfVsdFLlm6oYXwqvdE27Q'
api = 'RGAPI-61b2aecf-da19-4d68-b273-bae69dd6a000'
sum_id = '1VKY_8bB6g7agYYO_pZcieSe-Npy5iuV_t7L4jaZVquOC4k'
def get_puuid(gamename, tag, key):
    player = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gamename}/{tag}?api_key={key}')
    player = json.loads(player.text)
    return player['puuid']


def get_summ_id(puuid, key):
    summoner = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={key}')
    summoner = json.loads(summoner.text)
    return {'sumId': summoner['id'], 'level': summoner['summonerLevel'], 'icon':summoner['profileIconId']}

def get_player_data(summ_id, key):
    #list of match ids
    # rank, wr, role, champs, total games, icon, 
    player_data = {}
    summ_data = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summ_id}?api_key={key}').json()
    x=0
    for type in summ_data:
        if type['queueType'] == 'RANKED_SOLO_5x5':
            break
        x+=1

    player_data['rank'] = [summ_data[x]['tier'], summ_data[x]['rank'], summ_data[x]['leaguePoints']]
    player_data['wr'] = [summ_data[x]['wins'], summ_data[x]['losses']]

    return player_data



if __name__ == '__main__':
    sum = (get_summ_id(puuid, api))
    play = (get_player_data(sum_id, api))
    play.update(sum)
    print(play)

