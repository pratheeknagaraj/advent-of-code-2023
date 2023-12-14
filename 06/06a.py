#!/usr/bin/python3

from functools import reduce

with open('06_input', 'r') as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(':')[1].strip().split()]
distances = [int(x) for x in lines[1].split(':')[1].strip().split()]

races = zip(times, distances)

def run_race(race):
    win_count = 0
    for speed in range(0, race[0]+1):
        remaining_time = race[0]-speed
        distance = remaining_time * speed
        if distance > race[1]:
            win_count += 1
    return win_count

results = [run_race(r) for r in races]
product = reduce((lambda x, y: x * y), results)

print(product)
