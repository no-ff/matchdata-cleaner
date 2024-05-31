import requests
import time
from handle_riot_api_error import handle_riot_api_error

def convert(match_ids: list[str], api_key: str, file_name: str) -> str:
    startTime = time.time()
    h_counter = 0
    for match in match_ids:
        if h_counter == 100:
            currentTime = time.time()
            print("Time taken for 100 requests: " + str(currentTime - startTime) + " seconds.")
            print("Therefore we are going to sleep for "+str(120 - currentTime + startTime)+" seconds.")
            time.sleep(120.1 - currentTime + startTime)
            startTime = time.time()
            h_counter = 0
        h_counter += 1
        # Handle exceptions.
        move_on = False
        while True:
            match_info = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}")

            if handle_riot_api_error(match_info):
                move_on = True
                break

            match_info = match_info.json()
            break
        if move_on:
            continue

        temp = [0]
        for participant in match_info["info"]["participants"]:
            temp2 = []
            champ_tuple = (participant["championName"],
                           participant["championId"])
            temp2.append(champ_tuple)
            temp2.append(participant["teamId"])
            temp2.append(participant["teamPosition"])
            if temp2[1] == 100:
                temp[0] += participant["goldEarned"]
            else:
                temp[0] -= participant["goldEarned"]
            temp.append(temp2)

        # Append the winning team to the end.
        if len(match_info["info"]["participants"]) > 1:
            if match_info["info"]["participants"][0]["win"]:
                temp.append(100)
            else:
                temp.append(200)
        else:
            temp.append("error")

        temp.append(match)
        temp.append(match_info["info"]["gameDuration"])

        append_to_csv(temp, file_name)
        print(h_counter)


def append_to_csv(row: list, file_name: str) -> None:
    insert_row = ""
    for i in range(1, len(row)-3):
        insert_row += str(row[i][0][0]) + ","
    insert_row += str(row[0]) + "," + str(row[-3]) + \
        "," + str(row[-2]) + "," + str(row[-1])

    with open(file_name, 'a') as c:
        c.write(insert_row+"\n")
