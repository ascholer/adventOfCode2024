import functools
import re
from collections import defaultdict
import sys
import heapq

num_pad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None,'0','A']
]

ctrl_pad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

def get_data(fName):
    with open(fName, 'r') as f:
        return [line for line in f.read().split('\n')]

def make_str(s, n):
    if n == 0:
        return ''
    return s * n

def add_move_opts(move_opts, pad, is_num_pad=True):
    last_row = len(pad) - 1
    for r, list in enumerate(pad):
        for c, n in enumerate(list):
            if n is None:
                continue
            for r2, list in enumerate(pad):
                for c2, m in enumerate(list):
                    if m is None:
                        continue
                    if n == m:
                        move_opts[n+m] = ['A']
                        continue
                    r_dist = abs(r - r2)
                    c_dist = abs(c - c2)
                    l_r = "<" if c2 < c else ">"
                    u_d = "^" if r2 < r else "v"
                    paths = []

                    if is_num_pad and (n in ['1', '4', '7'] and m in ['0', 'A']):
                        paths.append( make_str(l_r, c_dist) + make_str(u_d, r_dist) + 'A')
                    elif is_num_pad and (n in ['0', 'A'] and m in ['1', '4', '7']):
                        paths.append(make_str(u_d, r_dist) + make_str(l_r, c_dist) + 'A')
                    elif (not is_num_pad) and (n in ['^', 'A'] and m == "<"):
                        paths.append(make_str(u_d, r_dist) + make_str(l_r, c_dist) + 'A')
                    elif (not is_num_pad) and (n == "<" and m in ['^', 'A']):
                        paths.append(make_str(l_r, c_dist) + make_str(u_d, r_dist) + 'A')
                    elif r_dist == 0 or c_dist == 0:
                        paths.append(make_str(u_d, r_dist) + make_str(l_r, c_dist) + 'A')
                    else:
                        paths.append(make_str(u_d, r_dist) + make_str(l_r, c_dist) + 'A')
                        paths.append(make_str(l_r, c_dist) + make_str(u_d, r_dist) + 'A')
                    move_opts[n+m] = paths

move_opts = {}
add_move_opts(move_opts, num_pad)
add_move_opts(move_opts, ctrl_pad, False)
for k, v in move_opts.items():
    print(k, v)

def make_steps(line):
    line = "A" + line
    steps = []
    for i in range(0, len(line) - 1):
        steps.append((line[i] + line[i+1]))
    return steps

foo = "159A"
s = make_steps(foo)
print(s)

def all_patterns(pattern, levels, so_far = ""):
    if levels == 0:
        print(pattern)
        return 
    steps = make_steps(pattern)
    opts = ['']
    for step in steps:
        new_opts = []
        for move in move_opts[step]:
            for o in opts:
                new_opts.append(o + move)
        opts = new_opts
    for opt in opts:
        all_patterns(opt, levels - 1)


def build_cache(levels):
    cache = {}
    for k, v in move_opts.items():
        cache[k] = min([len(x) for x in v])
    
    for l in range(levels):
        old_cache = cache
        cache = {}
        for k, v in move_opts.items():
            options = v
            best_cost = sys.maxsize
            for o in options:
                steps = make_steps(o)
                total = 0
                for step in steps:
                    total += old_cache[step]
                if total < best_cost:
                    best_cost = total
            cache[k] = best_cost
    return cache

def go(lines, levels = 25):
    cache = build_cache(levels)
    total = 0
    for line in lines:
        line_cost = 0
        for step in make_steps(line):
            line_cost += cache[step]
        num = int(line[0:3])
        # print(line_cost, num)
        total += line_cost * num
    print(total)

lines = get_data('data.txt')
go(lines, 2)
go(lines, 25)
