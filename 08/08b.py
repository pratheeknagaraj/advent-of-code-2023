#!/usr/bin/python3

import numpy as np

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

start_nodes = [n for n in nodes.keys() if n.endswith('A')]
cur_nodes = start_nodes

step_counts = []

for start_node in start_nodes:
    step_count = 0
    cur_node = start_node
    while True:
        direction = instructions[step_count % instructions_len]
        step_count += 1
        if direction == 'L':
            new_node = nodes[cur_node][0]
        else:
            new_node = nodes[cur_node][1]
        
        if new_node.endswith('Z'):
            step_counts.append(step_count)
            break

        cur_node = new_node

print(np.lcm.reduce(step_counts))
