import functools
import re
import copy
from collections import defaultdict

def get_data(fName):
    connections = defaultdict(list)
    with open(fName, 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            l, r = line.split('-')
            connections[l].append(r)
            connections[r].append(l)
    return connections

def find_connections(connects):
    nodes = connects.keys()
    groups = set()
    for node in nodes:
        # print(node)
        for conn in connects[node]:
            # print("  ", conn)
            for conn2 in connects[conn]:
                # print("    ", conn2)
                if conn2 != node and node in connects[conn2]:
                    group_list = [node, conn, conn2]
                    group_list.sort()
                    group_string = ",".join(group_list)
                    if group_string not in groups:
                        groups.add(group_string)
    return groups

def part1():
    c = get_data('data.txt')
    g = find_connections(c)
    gg = []
    for i in g:
        nodes = i.split(',')
        for n in nodes:
            if n[0] == 't':
                gg.append(i)
                break
    print(len(gg))

def pick_random(nodes):
    return nodes[random.randint(0, len(nodes) - 1)]

def shuffle(nodes):
    return random.shuffle(nodes)

import random
def get_rand_clique(connects):
    nodes = list(connects.keys())
    random_node = pick_random(nodes)
    clique = set()
    clique.add(random_node)
    node_con = connects[random_node]
    shuffle(node_con)
    for conn in node_con:
        in_clique = True
        for node in clique:
            if conn not in connects[node] or node not in connects[conn]:
                in_clique = False
                break
        if in_clique:
            clique.add(conn)
    return clique

def part2():
    connects = get_data('data.txt')
    largest = 0
    for i in range(0, 10000000):
        c = get_rand_clique(connects)
        if len(c) > largest:
            largest = len(c)
            l = list(c)
            l.sort()
            out = ",".join(l)
            print(out)
    # print(c)

part2()
