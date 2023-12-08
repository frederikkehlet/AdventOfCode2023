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

sum = 0
for game in games:

    greens = [int(round["value"]) for round in game["rounds"] if round["color"] == "green"]
    reds = [int(round["value"]) for round in game["rounds"] if round["color"] == "red"]
    blues = [int(round["value"]) for round in game["rounds"] if round["color"] == "blue"]

    max_green = max(greens) if len(greens) != 0 else 1;
    max_red = max(reds) if len(reds) != 0 else 1;
    max_blue = max(blues) if len(blues) != 0 else 1;

    sum += (max_green * max_red * max_blue)

print(sum)

