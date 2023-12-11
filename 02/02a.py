#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

RED = 12
GREEN = 13
BLUE = 14

id_sum = 0

for l in lines:
    success = True
    cl = l.strip()

    id_num = int(cl.split(':')[0].split(' ')[1])
    draws = cl.split(':')[1].strip().split(';')

    for d in draws:
        parts = [s.strip() for s in d.split(',')]
        for p in parts:
            num = int(p.split(' ')[0])
            color = p.split(' ')[1]

            if color == 'red':
                if num > RED:
                    success = False
            elif color == 'green':
                if num > GREEN:
                    success = False
            elif color == 'blue':
                if num > BLUE:
                    success = False

    if success:
        id_sum += id_num

print(id_sum)
