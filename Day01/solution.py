# part 1
f = open("input.txt", "r")
lines = f.readlines()

# sum = 0

# for line in lines:
#     digits = []
#     chars = list(line)
    
#     for c in chars:
#         if c.isdigit():
#             digits.append(c)

#     value = ""
#     if len(digits) == 1:
#         value = str(digits[0] + digits[0])
#     else:
#         value = str(digits[0] + digits[len(digits)-1])

#     sum += int(value)
    
# print(sum)

# part 2
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    digits = []
    index = 0
    for word in words:
        if line[index:len(word)] == word:
            digits.append(word)
            index = index + (len(word) - 1)
    print(digits)
