#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

def process_card(line):
    winning_nums = set([int(i) for i in line.strip().split('|')[0].split(':')[1].split()])
    my_nums = set([int(i) for i in line.strip().split('|')[1].split()])

    win_count = len(winning_nums.intersection(my_nums))
    return win_count

cards = [1]*len(lines)

for i, l in enumerate(lines):
    wins = process_card(l)
    multiple = cards[i]
    for j in range(i+1, i+1+wins):
        cards[j] += multiple

print(sum(cards))
