import re

f = open("input.txt", "r")
lines = f.readlines()

def retrieve_left_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y]) if match.end()-1 == x]
    return int(match[-1]["value"]) if len(match) != 0 else None

def retrieve_right_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y]) if match.start() == x+1]
    return int(match[0]["value"]) if len(match) != 0 else None

def retrieve_top_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y-1]) if match.start() <= x and match.end()-1 >= x]
    return int(match[0]["value"]) if len(match) != 0 else None

def retrieve_bottom_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y+1]) if match.start() <= x and match.end()-1 >= x]
    return int(match[0]["value"]) if len(match) != 0 else None

def retrieve_top_diagonally_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y-1]) if match.end() == x or match.start() == x+1]
    return int(match[0]["value"]) if len(match) != 0 else None

def retrieve_bottom_diagonally_adjacent(x,y):
    match = [{"value": match.group()} for match in re.finditer('\d+',lines[y+1]) if match.end() == x or match.start() == x+1]
    return int(match[0]["value"]) if len(match) != 0 else None

def retrieve_adjacent_numbers(x,y):
    numbers = []
    num = retrieve_left_adjacent(x,y)
    if num != None: numbers.append(num)

    num = retrieve_right_adjacent(x,y)
    if num != None: numbers.append(num)

    num = retrieve_top_adjacent(x,y)
    if num != None: 
        numbers.append(num)
    else:
        num = retrieve_top_diagonally_adjacent(x,y)
        if num != None:
            numbers.append(num)

    num = retrieve_bottom_adjacent(x,y)
    if num != None: 
        numbers.append(num)
    else:
        num = retrieve_bottom_diagonally_adjacent(x,y)
        if num != None: 
            numbers.append(num)
    
    return numbers

sum = 0
y = x = 0
for line in lines:
    chars = list(line)

    for c in chars:
        if c == "*":
            numbers = retrieve_adjacent_numbers(x,y)
            print(numbers)
            if len(numbers) == 2:
                product = (numbers[0] * numbers[1])
                sum += product
                

        x = x + 1

    x = 0
    y = y + 1

print(sum)