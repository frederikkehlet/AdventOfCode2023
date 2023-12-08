f = open("input.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    digits = []
    chars = list(line)
    
    for c in chars:
        if c.isdigit():
            digits.append(c)
            
    sum += int(str(digits[0]) + str(digits[-1]))
    
print(sum)


