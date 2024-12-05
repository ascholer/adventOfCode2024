import functools
import re

def get_data(fName):
    with open(fName, 'r') as f:
        data = f.read()
        return data

def part1(data):
    total = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data, re.MULTILINE)
    # print(matches)
    for match in matches:
        total += int(match[0]) * int(match[1])
    print(total)

def part2(data):
    total = 0
    do = True
    pattern = r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do(?:n't)?\(\))"
    matches = re.findall(pattern, data, re.MULTILINE)
    # print(matches)
    for match in matches:
        if match[2] == '' and do:
            total += int(match[0]) * int(match[1])
        elif match[2] == 'do()':
            do = True
        elif match[2] == "don't()":
            do = False
    print(total)

data = get_data('data.txt')
part1(data)
part2(data)