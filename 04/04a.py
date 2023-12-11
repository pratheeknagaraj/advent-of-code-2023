#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

def process_card(line):
    winning_nums = set([int(i) for i in line.strip().split('|')[0].split(':')[1].split()])
    my_nums = set([int(i) for i in line.strip().split('|')[1].split()])

    overlap = len(winning_nums.intersection(my_nums))

    if overlap:
        return 2**(overlap-1)
    return 0

points = []
for l in lines:
    points.append(process_card(l))

print(sum(points))
