import re

f = open("input.txt", "r")
lines = f.readlines()
width = len(lines[1])-1

def get_bounding_box(index,start,end):
    bounding_box = []
    if index == 0:
        if start == 0:
            [bounding_box.append(l) for l in lines[index][end]]
            [bounding_box.append(l) for l in lines[index+1][start:end+1]]
            return bounding_box

        if end == width:
            [bounding_box.append(l) for l in lines[index][start-1]]
            [bounding_box.append(l) for l in lines[index+1][start-1:]]
            return bounding_box
        
        [bounding_box.append(l) for l in lines[index][start-1]]
        [bounding_box.append(l) for l in lines[index][end]]
        [bounding_box.append(l) for l in lines[index+1][start-1:end+1]]
        return bounding_box
        
    if index == len(lines)-1:
        if start == 0:
            [bounding_box.append(l) for l in lines[index-1][start:end+1]]
            [bounding_box.append(l) for l in lines[index][end]]
            return bounding_box
        
        if end == width:
            [bounding_box.append(l) for l in lines[index-1][start-1:]]
            [bounding_box.append(l) for l in lines[index][start-1]]
            return bounding_box
        
        [bounding_box.append(l) for l in lines[index][start-1]]
        [bounding_box.append(l) for l in lines[index][end]]
        [bounding_box.append(l) for l in lines[index-1][start-1:end+1]]
        return bounding_box

    if start == 0:
        [bounding_box.append(l) for l in lines[index-1][start:end+1]]
        [bounding_box.append(l) for l in lines[index][end]]
        [bounding_box.append(l) for l in lines[index+1][start:end+1]]
        return bounding_box
    
    if end == width:
        [bounding_box.append(l) for l in lines[index-1][start-1:end]]
        [bounding_box.append(l) for l in lines[index][start-1]]
        [bounding_box.append(l) for l in lines[index+1][start-1:end]]
        return bounding_box

    [bounding_box.append(l) for l in lines[index][start-1]]
    [bounding_box.append(l) for l in lines[index-1][start-1:end+1]]
    [bounding_box.append(l) for l in lines[index][end]]
    [bounding_box.append(l) for l in lines[index+1][start-1:end+1]]
    return bounding_box

sum = 0
for line in lines:
    index = lines.index(line)

    matches = [{"v": int(m.group()), "s": m.start(), "e": m.end()} for m in re.finditer('\d+',line)]

    for match in matches:
        box = get_bounding_box(index,match["s"], match["e"])
        sum += match["v"] if re.search(r'[^.\d\n]',''.join(box)) != None else 0
    
print(sum)

    