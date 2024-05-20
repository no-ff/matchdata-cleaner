import requests
import time

def convert(match_ids: list[str], api_key: str, file_name: str) -> str:
    for match in match_ids:
        #handles rate limits, when limit is hit, it keeps on trying, until the limit is gone
        while True:
            match_info = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" %(match, api_key))
            if match_info.status_code == 429:
                print("Rate Limit Exceeded, gonna sleep a bit")
                time.sleep(20)
                continue
            match_info = match_info.json()
            break

        temp = [0]
        for participant in match_info["info"]["participants"]:
            temp2 = []
            champ_tuple = (participant["championName"], participant["championId"])
            temp2.append(champ_tuple)
            temp2.append(participant["teamId"])
            temp2.append(participant["teamPosition"])
            if temp2[1] == 100:
                temp[0] += participant["goldEarned"]
            else:
                temp[0] -= participant["goldEarned"]
            temp.append(temp2)

        #appends the winning team to the end
        if match_info["info"]["participants"][0]["win"]:
            temp.append(100)
        else:
            temp.append(200)   

        temp.append(match)
        append_to_csv(temp, file_name)


def append_to_csv(row: list, file_name: str)-> None:
    insert_row = ""
    for i in range(1, len(row)-2):
        insert_row += str(row[i][0][0]) + ","
    insert_row += str(row[0]) + "," + str(row[-2])+ ","+ str(row[-1])

    with open(file_name, 'a') as c:
        c.write(insert_row+"\n")




