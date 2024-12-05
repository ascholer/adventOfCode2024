import functools

def get_data(fName):
    lines = []
    with open(fName, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    listA = []
    listB = []
    for line in lines:
        [a, b] = line.split('   ')
        listA.append(int(a))
        listB.append(int(b))
    return [listA, listB]

def part1(data):
    [listA, listB] = data
    listA.sort()
    listB.sort()
    diffs = map(lambda x: abs(x[0] - x[1]), zip(listA, listB))
    sum = functools.reduce(lambda x, y: x + y, diffs)
    print(sum)

def part2(data):
    [listA, listB] = data
    sum = 0
    for a in listA:
        similarity = a * len(list(filter(lambda x: x == a, listB)))
        sum += similarity
    print(sum)

data = get_data('data.txt')
part1(data)
part2(data)