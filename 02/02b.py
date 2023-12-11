#!/usr/bin/python3

import math

with open('02_input', 'r') as f:
    lines = f.readlines()

power_sum = 0

for l in lines:
    success = True
    cl = l.strip()

    draws = cl.split(':')[1].strip().split(';')

    min_red = 0
    min_green = 0
    min_blue = 0

    for d in draws:
        parts = [s.strip() for s in d.split(',')]
        for p in parts:
            num = int(p.split(' ')[0])
            color = p.split(' ')[1]

            if color == 'red':
                min_red = max(min_red, num)
            elif color == 'green':
                min_green = max(min_green, num)
            elif color == 'blue':
                min_blue = max(min_blue, num)

    if success:
        power_sum += (min_red * min_green * min_blue)

print(power_sum)
