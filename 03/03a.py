#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

x_max = len(lines[0])
y_max = len(lines)

def check_for_symbol(xs, y, integer):
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
            if not lines[j][i].isdigit() and lines[j][i] != '.' and lines[j][i] != '\n':
                return True

    return False

part_numbers = []

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
            if check_for_symbol(xs, j, integer):
                part_numbers.append(integer)

            num = ''
            xs = []

    if num != '':
        integer = int(num)
        if check_for_symbol(xs, j, integer):
            part_numbers.append(integer)

print(sum(part_numbers))
