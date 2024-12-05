import functools
import re

def get_data(fName):
    with open(fName, 'r') as f:
        lines = f.read().split('\n')
        data = list(map(lambda x: list(x), lines))
        return data

def rotate_clockwise(data):
    rot_tuples = zip(*data[::-1])
    rot_list = [list(i) for i in rot_tuples]
    return rot_list

def check_hor(data, x, y):
    if x + 3 >= len(data[y]):
        print('no hor', x, y)
        return False
    if data[y][x + 1] == 'M' and data[y][x + 2] == 'A' and data[y][x + 3] == 'S':
        space[y][x + 1] = 'X'
        space[y][x + 2] = 'X'
        space[y][x + 3] = 'X'
        return True
    return False

def check_dia_right(data, x, y):
    global space
    if x + 3 >= len(data[y]) or y + 3 >= len(data):
        return False
    if data[y + 1][x + 1] == 'M' and data[y + 2][x + 2] == 'A' and data[y + 3][x + 3] == 'S':
        space[y + 1][x + 1] = 'X'
        space[y + 2][x + 2] = 'X'
        space[y + 3][x + 3] = 'X'
        return True
    return False

def check_dia_left(data, x, y):
    global space
    if x < 3 or y + 3 >= len(data):
        return False
    if data[y + 1][x - 1] == 'M' and data[y + 2][x - 2] == 'A' and data[y + 3][x - 3] == 'S':
        return True
    return False

space = [[0 for x in range(140)] for y in range(140)]

def scan(data):
    global space
    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'X':
                if check_hor(data, x, y):
                    space[y][x] = 'X'
                    print('hor', y, x)
                    total += 1
                if check_dia_right(data, x, y):
                    space[y][x] = 'X'
                    print('dia_r', y, x)
                    total += 1
                # if check_dia_left(data, j, i):
                #     print('dia_l', i, j)
                #     total += 1
    print(total)
    return total

def part1(data):
    global space
    total = scan(data)
    # for line in space:
    #     print(line)
    # print("rotate")
    data = rotate_clockwise(data)
    space = rotate_clockwise(space)
    total += scan(data)
    
    # for line in space:
    #     print(line)
    space = rotate_clockwise(space)
    # print("rotate")
    data = rotate_clockwise(data)
    total += scan(data)
    # for line in space:
    #     print(line)
    space = rotate_clockwise(space)
    # print("rotate")
    data = rotate_clockwise(data)
    total += scan(data)
    # print(total)
    space = rotate_clockwise(space)
    # print(space)
    # print("==========")
    # for line in space:
    #     print(line)

    print(total)

data = get_data('data.txt')
part1(data)