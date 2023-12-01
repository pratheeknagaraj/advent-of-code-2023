#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

total = 0

for l in lines:
    first = None
    last = None

    for c in l:
        if c.isdigit():
            if first is None:
                first = c
            last = c

    num = int(first + last)
    total += num

print(total)
