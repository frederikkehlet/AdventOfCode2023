import re
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

f = open("input.txt", "r")
lines = f.readlines()

def convertToNumber(numWord):
    if numWord == "one": return "1"
    if numWord == "two": return "2"
    if numWord == "three": return "3"
    if numWord == "four": return "4"
    if numWord == "five": return "5"
    if numWord == "six": return "6"
    if numWord == "seven": return "7"
    if numWord == "eight": return "8"
    if numWord == "nine": return "9"

sum = 0

for line in lines:
    numbers = []
    matches = [{"value": match.group(), "index": match.start()} for match in re.finditer(r'\d+', line)]

    if matches:
        for match in matches:
            numbers.append(match)

    for word in words:
        matches = [{"value": convertToNumber(match.group()), "index": match.start()} for match in re.finditer(word, line)]

        if matches:
            for match in matches:
                numbers.append(match)

    numbers.sort(key=lambda x: x["index"])
    calibration_value = numbers[0]["value"][0] + numbers[-1]["value"][-1]
    
    sum += int(calibration_value)

print(sum)




