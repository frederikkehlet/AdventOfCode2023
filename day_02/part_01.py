f = open("input.txt", "r")
lines = f.readlines()

red_cubes = 12
green_cubes = 13
blue_cubes = 14

games = []
for line in lines:
    game = {}

    game["id"] = line.split(":")[0].split(" ")[-1]
    game["rounds"] = []

    rounds = line.split(":")[1].split(";")
    rounds = [round.strip() for round in rounds]

    for round in rounds:
        sets = round.split(",")
        sets = [set.strip() for set in sets]

        for set in sets:
            cubes = set.split(" ")
            game["rounds"].append({"value": int(cubes[0]), "color": cubes[1]})

    games.append(game)

ids = []
for game in games:
    valid_game = True
    for round in game["rounds"]:
        if round["color"] == "blue" and round["value"] > blue_cubes:
            valid_game = False
            break
        if round["color"] == "red" and round["value"] > red_cubes:
            valid_game = False
            break
        if round["color"] == "green" and round["value"] > green_cubes:
            valid_game = False
            break
    
    if valid_game:
        ids.append(int(game["id"]))

print(sum(ids))