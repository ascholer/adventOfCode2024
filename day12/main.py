import functools
import re
import copy
from collections import defaultdict

def get_data(fName):
    with open(fName, 'r') as f:
        data = f.read()
        return [list(x) for x in data.split('\n')]

def explore(map, i, j):
    area = 0
    perimeter = 0
    start_type = map[i][j]
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[i]):
            perimeter += 1
            # print('oob' , i, j, start_type)
            continue
        if map[i][j] == start_type.lower():
            continue
        if map[i][j] != start_type:
            perimeter += 1
            # print('not' , i, j, start_type)
            continue
        area += 1
        map[i][j] = start_type.lower()
        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))
    # print(start_type, area, perimeter)
    return area, perimeter


def explore2(map, i, j):
    area = 0
    start_type = map[i][j]
    stack = [(i, j)]
    perim_set = set()
    area_set = set()
    while stack:
        i, j = stack.pop()
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[i]):
            perim_set.add((i, j))
            continue
        if map[i][j] == start_type.lower():
            continue
        if map[i][j] != start_type:
            perim_set.add((i, j))
            continue
        area_set.add((i, j))
        map[i][j] = start_type.lower()
        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))
    
    # print("a", area_set)
    # print("p", perim_set)

    new_type = start_type.lower()
    sides = []
    for location in area_set:
        i, j = location
        left = (i, j - 1)
        left_up = (i - 1, j - 1)
        left_down = (i + 1, j - 1)
        right = (i, j + 1)
        right_up = (i - 1, j + 1)
        up = (i - 1, j)
        down = (i + 1, j)

        if start_type == "S":
            x = 1

        if left in perim_set:
            if not (up in area_set and left_up in perim_set):
                sides.append(location)
        if right in perim_set:
            if not (up in area_set and right_up in perim_set):
                sides.append(location)
        if up in perim_set:
            if not (left in area_set and left_up in perim_set):
                sides.append(location)
        if down in perim_set:
            if not (left in area_set and left_down in perim_set):
                sides.append(location)

    # print("s", sides)
    area = len(area_set)
    num_sides = len(sides)
    for location in area_set:
        map[location[0]][location[1]] = "#"
    # print(start_type, area, num_sides)
    return area, num_sides

def print_map(map):
    for row in map:
        print(''.join(row))
    print()

def part1(map):
    map = map.copy()
    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].isupper():
                area, perimeter = explore(map, i, j)
                total += area * perimeter
    print(total)


def part2(map):
    map = map.copy()
    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].isupper():
                area, sides = explore2(map, i, j)
                # print_map(map)
                total += area * sides
    print(total)

data = get_data('data.txt')
# print(data)
part1(copy.deepcopy(data))
part2(data)