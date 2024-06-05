import random
f = open("albert.csv", "r")
output = open("new.csv", "w")
for line in f:
    data = line.split(",")
    data.pop(1)
    data.pop(5)
    team1 = data[:4]
    team2 = data[4:8]

    rteam1 = []
    rteam2 = []
    random_lst = random.sample(range(0, 4), 4)
    for i in random_lst:
        rteam1.append(team1[i])
        rteam2.append(team2[i])

    new_team1 = "".join(x + "," for x in rteam1)
    new_team11 = "".join(x + "," for x in team1)

    new_team2 = "".join(x + "," for x in rteam2)
    new_team22 = "".join(x + "," for x in team2)

    output.write(new_team1 + new_team11 + "\n")
    output.write(new_team2 + new_team22 + "\n")
    