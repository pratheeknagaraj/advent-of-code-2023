#!/usr/bin/python3

import math

with open('06_input', 'r') as f:
    lines = f.readlines()

time = int(lines[0].split(':')[1].strip().replace(' ',''))
distance = int(lines[1].split(':')[1].strip().replace(' ',''))

def run_race(time, distance):

    # Solutions are:
    # (time - x) * x > distance
    # 
    # Solve for x:
    #   (time - x) * x = distance
    #   x^2 - time * x + distance = 0
    #   x = (time +/- sqrt(time^2 - 4*distance)) / 2
    #
    # Boundary solutions are:
    #   x_1 = ceil((time - sqrt(time^2 - 4*distance))/2)
    #   x_2 = floor((time + sqrt(time^2 - 4*distance))/2)

    inner = math.sqrt(math.pow(time, 2.0) - 4 * distance)
    x1 = math.ceil((time - inner)/2)
    x2 = math.floor((time + inner)/2)

    solutions = x2 - x1 + 1
    return solutions

result = run_race(time, distance)

print(result)
