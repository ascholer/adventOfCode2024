import functools
import re
import copy
from collections import defaultdict

def get_data(fName):
    with open(fName, 'r') as f:
        data = f.read()
        return [int(x) for x in data.split('\n')]

def evolve(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n

def xform(n, steps):
    for i in range(steps):
        n = evolve(n)
    return n

global_cache = defaultdict(int)
def xform_track(n, steps):
    orig_n = n
    local_cache = {}
    last4 = []
    for i in range(steps):
        old_last_digit = n % 10
        n = evolve(n)
        last_digit = n % 10
        delta = last_digit - old_last_digit
        last4.append(delta)
        if i >= 3:
            if i > 3:
                last4.pop(0)
            l_4 = tuple(last4)
            if l_4 not in local_cache:
                # if l_4 == (-2,1,-1,3):
                #     print(i, last_digit, orig_n)
                # print(i, last_digit, n)
                local_cache[l_4] = last_digit
        
    global global_cache
    for k, v in local_cache.items():
        global_cache[k] += v

def part1(data):
    total = 0
    for n in data:
        total += xform(n, 2000)
    print(total)

def part2(data):
    total = 0
    for n in data:
        xform_track(n, 2000)
    max = 0
    global global_cache
    print(global_cache[(-2,-1,-1,3)])
    for k, v in global_cache.items():
        if v > max:
            max = v
            print(k, v)
    print(total)

data = get_data('data.txt')
#part1(data)
part2(data)