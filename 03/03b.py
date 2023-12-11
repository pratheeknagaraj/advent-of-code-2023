#!/usr/bin/python3

from collections import defaultdict

with open('03_input', 'r') as f:
    lines = f.readlines()

x_max = len(lines[0])
y_max = len(lines)

def check_for_gear(xs, y, integer):
    checks = []
    min_xs = min(xs)
    max_xs = max(xs)

    for j in (y-1, y+1):
        for i in range(min_xs-1, max_xs+2):
            checks.append((i,j))
    checks.append((min_xs-1,y))
    checks.append((max_xs+1,y))
    
    for c in checks:
        i, j = c
        if i >= 0 and i < x_max and j >= 0 and j < y_max:
            if lines[j][i] == '*':
                return (i,j)

    return None

gear_grid = defaultdict(list)

for j, l in enumerate(lines):
    num = ''
    xs = []
    for i, c in enumerate(l.strip()):
        if c.isdigit():
            num += c
            xs.append(i)
        elif num == '':
            continue
        else:
            integer = int(num)
            ret = check_for_gear(xs, j, integer)
            if ret:
                gear_grid[ret].append(integer)

            num = ''
            xs = []

    if num != '':
        integer = int(num)
        ret = check_for_gear(xs, j, integer)
        if ret:
            gear_grid[ret].append(integer)

ratios = []

for nums in gear_grid.values():
    if len(nums) == 2:
        ratios.append(nums[0] * nums[1])

print(sum(ratios))
