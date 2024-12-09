import functools
import re
from collections import defaultdict

size = 10

def get_data(fName):
    antennas = defaultdict(list)
    with open(fName, 'r') as f:
        lines = f.read().split('\n')
        global size
        size = len(lines)
        for r in range(len(lines)):
            line = lines[r]
            for c in range(len(line)):
                if line[c] != '.':
                    antennas[line[c]].append((r, c))
    return antennas

def in_bounds(loc):
    global size
    r, c = [*loc]
    return 0 <= r < size and 0 <= c < size

def part1(antennas):
    antinodes = set()
    for type in antennas:
        # print (type)
        # print (antennas[type])
        for i in range(len(antennas[type])):
            for j in range(i+1, len(antennas[type])):
                r1, c1 = antennas[type][i]
                r2, c2 = antennas[type][j]
                ydiff = r2 - r1
                xdiff = c2 - c1
                # print("----------")
                # print(r1, c1)
                # print(r2, c2)
                # print(r1 - ydiff, c1 - xdiff)
                # print(r2 + ydiff, c2 + xdiff)
                antinode1 = (r1 - ydiff, c1 - xdiff)
                if in_bounds(antinode1):
                    antinodes.add(antinode1)
                antinode2 = (r2 + ydiff, c2 + xdiff)
                if in_bounds(antinode2):
                    antinodes.add(antinode2)
    print(len(antinodes))

def print_grid(antinodes):
    global size
    for r in range(size):
        for c in range(size):
            if (r, c) in antinodes:
                print('X', end='')
            else:
                print('.', end='')
        print()

def part2(antennas):
    antinodes = set()
    for type in antennas:
        for i in range(len(antennas[type])):
            if len(antennas[type]) > 1:
                antinodes.add(antennas[type][i])
            for j in range(i+1 , len(antennas[type])):
                r1, c1 = antennas[type][i]
                r2, c2 = antennas[type][j]
                ydiff = r2 - r1
                xdiff = c2 - c1
                antinode1 = (r1 - ydiff, c1 - xdiff)
                while in_bounds(antinode1):
                    antinodes.add(antinode1)
                    antinode1 = (antinode1[0] - ydiff, antinode1[1] - xdiff)
                antinode2 = (r2 + ydiff, c2 + xdiff)
                while in_bounds(antinode2):
                    antinodes.add(antinode2)
                    antinode2 = (antinode2[0] + ydiff, antinode2[1] + xdiff)
    # print_grid(antinodes)
    print(len(antinodes))

data = get_data('data.txt')
part1(data)
part2(data)