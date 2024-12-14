import functools
import re
from collections import defaultdict

def get_data(fName):
    stones = defaultdict(int)
    with open(fName, 'r') as f:
        data = f.read()
        for x in [int(x) for x in data.split(' ')]:
            stones[x] += 1
        return stones

def blink(stones):
    new_stones = defaultdict(int)
    for stone in stones:
        stone_count = stones[stone]
        if stone == 0:
            new_stones[1] += stone_count
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            stone1 = int(str_stone[:len(str_stone) // 2])
            stone2 = int(str_stone[len(str_stone) // 2:])
            new_stones[stone1] += stone_count
            new_stones[stone2] += stone_count
        else:
            new_stones[stone * 2024] = stone_count
    return new_stones

def part(stones, n):
    for i in range(n):
        stones = blink(stones)
    count = functools.reduce(lambda x, y: x + y, stones.values())
    print(n, count)


data = get_data('data.txt')
# print(data)
part(data, 25)
part(data, 75)