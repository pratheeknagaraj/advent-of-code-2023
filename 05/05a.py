#!/usr/bin/python3

with open('05_input', 'r') as f:
    lines = f.readlines()

seeds = []

handle_map = False
map_lines = []
map_name = None
map_directions = {}
maps = {}

def create_map(map_lines):
    ranges = []
    for l in map_lines:
        ranges.append((l[1], l[1]+l[2]-1, -l[1]+l[0]))
    ranges = sorted(ranges, key=lambda x: x[0])
    return ranges

for line in lines:
    l = line.strip()
    if 'seeds' in l:
        seeds = [int(s) for s in l.split(':')[1].strip().split()]
        continue
    elif 'map' in l:
        handle_map = True
        parts = l.split('map')[0].strip().split('-')
        map_name = (parts[0], parts[2])
        continue
    elif handle_map:
        if l != '':
            map_lines.append([int(i) for i in l.split()])
        else:
            maps[map_name] = create_map(map_lines)
            map_directions[map_name[0]] = map_name[1]

            handle_map = False
            map_lines = []
            map_name = None
            continue

maps[map_name] = create_map(map_lines)
map_directions[map_name[0]] = map_name[1]

start_pos = 'seed'
end_pos = 'location'

def find_location(seed):
    pos = start_pos
    num = seed

    while pos != end_pos:
        map_start = pos
        map_end = map_directions[pos]
        map_name = (map_start, map_end)
        ranges = maps[map_name]

        new_num = num
        for r in ranges:
            if num >= r[0] and num <= r[1]:
                new_num = num + r[2]
                break
        num = new_num
        pos = map_end

    return num


locations = []
for s in seeds:
    location = find_location(s)
    locations.append(location)

print(min(locations))

