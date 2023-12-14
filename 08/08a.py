#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

instructions = lines[0].strip()
instructions_len = len(instructions)

map_lines = lines[2:]
nodes = {}
for l in map_lines:
    start, ends = l.strip().split('=')
    start = start.strip()
    ends = ends.strip()
    end_tuple = (ends[1:4], ends[6:9])
    nodes[start] = end_tuple

cur = 'AAA'
end = 'ZZZ'

step_count = 0
while True:
    direction = instructions[step_count % instructions_len]
    step_count += 1
    if direction == 'L':
        new_node = nodes[cur][0]
    else:
        new_node = nodes[cur][1]
    if new_node == end:
        break
    cur = new_node

print(step_count)
