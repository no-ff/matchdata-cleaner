import requests
import time


def convert(match_ids: list[str], api_key: str, file_name: str) -> str:
    startTime = time.time()
    for match in match_ids:

        # Handle exceptions.
        move_on = False
        while True:
            match_info = requests.get(
                "https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" % (match, api_key))
            if match_info.status_code == 429:
                print(f"The following error code has been invoked:{match_info.status_code} sleeping for 2 minutes")
                time.sleep(120)
                continue
            if match_info.status_code == 400 or \
                    match_info.status_code == 403 or \
                    match_info.status_code == 401 or \
                    match_info.status_code == 404 or \
                    match_info.status_code == 405 or\
                    match_info.status_code == 415:
                print(f"The following error code has been invoked:{match_info.status_code}")
                move_on = True
                break

            if match_info.status_code == 500 or \
                    match_info.status_code == 502 or \
                    match_info.status_code == 503 or \
                    match_info.status_code == 504:
                print(f"The following error code has been invoked:{match_info.status_code} sleeping for 2 minutes")
                time.sleep(120)
                continue

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
        print(time.time() - startTime)
        time.sleep(0.65)


def append_to_csv(row: list, file_name: str) -> None:
    insert_row = ""
    for i in range(1, len(row)-3):
        insert_row += str(row[i][0][0]) + ","
    insert_row += str(row[0]) + "," + str(row[-3]) + \
        "," + str(row[-2]) + "," + str(row[-1])

    with open(file_name, 'a') as c:
        c.write(insert_row+"\n")
