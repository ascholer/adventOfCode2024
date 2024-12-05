import functools

def get_data(fName):
    lines = []
    with open(fName, 'r') as f:
        lines = f.readlines()
    data = [[int(a) for a in line.split()] for line in lines]
    #print(data)
    return data

def part1(data):
    safe_count = 0
    for report in data:
        if report[0] > report[1]:
            report.reverse()
        safe = True
        for i in range(len(report) - 1):
            diff = report[i+1] - report[i]
            if diff < 1 or diff > 3:
                safe = False
                break
        if safe:
            safe_count += 1
    print(safe_count)

def check_report(report):
    issues = 0
    i = 0
    while i < len(report) - 1:
        diff = report[i + 1] - report[i]
        if diff < 1 or diff > 3:
            issues += 1
            if issues > 1:
                break
            skip_next = i == len(report) - 2 or 4 > report[i + 2] - report[i] > 0
            skip_cur = i == 0 or 4 > report[i + 1] - report[i - 1] > 0
            if not (skip_next or skip_cur):
                issues += 1
                break
            if skip_next:
                i += 1
        i += 1
    return issues <= 1

def part2(data):
    safe_count = 0
    for report in data:
        safe = check_report(report)
        if not safe:
            report.reverse()
            safe = check_report(report)

        if safe:
            safe_count += 1

    print(safe_count)

data = get_data('data.txt')
part1(data.copy())
part2(data)