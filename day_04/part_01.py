import re
f = open("input.txt", "r")
lines = f.readlines()

sum = 0
for line in lines:
    winning_numbers = [int(match.group()) for match in re.finditer('\d+',line.split(" | ")[0].split(":")[1])]
    card_numbers = [int(match.group()) for match in re.finditer('\d+',line.split(" | ")[1])]
    
    matches = 0
    for num in card_numbers:
        if num in winning_numbers: # match
            if matches <= 1: matches += 1 
            else: matches = matches * 2
        
    sum += matches

print(sum)