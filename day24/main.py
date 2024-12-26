import functools
import re
import copy
from collections import defaultdict

def get_data(fName):
    gates = {}
    values = {}
    with open(fName, 'r') as f:
        value_data, gate_data = f.read().split('\n\n')
        for line in value_data.split('\n'):
            k, v = line.split(': ')
            values[k] = bool(int(v))
        for line in gate_data.split('\n'):
            source, target = line.split(' -> ')
            op1, op, op2 = source.split(' ')
            gates[target] = {'op':op, 'op1':op1, 'op2': op2}
    return values, gates

def get_value(values, gates, key):
    if key in values:
        return values[key]
    gate = gates[key]
    op = gate['op']
    op1 = get_value(values, gates, gate['op1'])
    op2 = get_value(values, gates, gate['op2'])
    if gate['op'] == 'AND':
        return op1 & op2
    if gate['op'] == 'OR':
        return op1 | op2
    if gate['op'] == 'XOR':
        return op1 ^ op2

def num_digits(gates):
    return len([1 for k in gates.keys() if k[0] == 'z'])

def part1(values, gates):
    out = ""
    total = 0
    n = num_digits(gates)
    for i in range(n - 1, -1, -1):
        value = get_value(values, gates, f'z{i:02d}')
        print (f'z{i:02d}', value)
        out += str(int(value))
        total += value * (2 ** (i))
    print(out)
    print(total)

def simplify(gate, gates):
    if type(gate) == str:
        if gate[0] in ['x', 'y']:
            return gate
        gate = gates[gate]
    op = gate['op']
    op1 = gate['op1']
    if 'op2' in gate:
        op2 = gate['op2']
    if op == 'XOR':
        op = 'OR'
        nop1 = {'op': 'NOT', 'op1': op1}
        nop2 = {'op': 'NOT', 'op1': op2}
        op1 = {'op': 'AND', 'op1': op1, 'op2': nop2}
        op2 = {'op': 'AND', 'op1': nop1, 'op2': op2}
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'OR':
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'AND':
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'NOT':
        op1 = simplify(op1, gates)
        return {'op': op, 'op1': op1}


def simplify2(gate, gates):
    if type(gate) == str:
        if gate[0] in ['x', 'y']:
            return gate
        gate = gates[gate]
    op = gate['op']
    op1 = gate['op1']
    if 'op2' in gate:
        op2 = gate['op2']
    if op == 'XAND':
        op = 'OR'
        nop1 = {'op': 'NOT', 'op1': op1}
        nop2 = {'op': 'NOT', 'op1': op2}
        op1 = {'op': 'AND', 'op1': op1, 'op2': nop2}
        op2 = {'op': 'AND', 'op1': nop1, 'op2': op2}
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'OR':
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'AND':
        op1 = simplify(op1, gates)
        op2 = simplify(op2, gates)
        return {'op': op, 'op1': op1, 'op2': op2}
    elif op == 'NOT':
        op1 = simplify(op1, gates)
        return {'op': op, 'op1': op1}
    
    if 'op2' in gate:
        return {'op': op, 'op1': op1, 'op2': op2}
    return {'op': op, 'op1': op1}

def iprint(g, indent=""):
    if type(g) == str:
        print(f'{indent}{g}')
    else:
        print(f'{indent}{g["op"]}')
        iprint(g["op1"], indent + "  ")
        if 'op2' in g:
            iprint(g["op2"], indent + "  ")

def part2(values, gates):
    out = ""
    total = 0
    n = num_digits(gates)
    for k, g in gates.items():
        # x = simplify(g, gates)
        op1 = g['op1']
        op2 = g['op2']
        if re.match(r'[xy]\d+', op1) and re.match(r'[xy]\d+', op2):
            # x = simplify(g, gates)
            print(k)
            iprint(g)
        # print(k)
        # iprint(x)
    # for i in range(0, 1, 1):
    #     g = gates[f'z{i:02d}']
    #     g = simplify(g, gates)
        # g = simplify2(g, gates)
        # iprint(g)
    # print(out)
    # print(total)

values, gates = get_data('sample.txt')
# part1(values, gates)
part2(values, gates)