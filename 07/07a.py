#!/usr/bin/python3

from collections import Counter
from functools import cmp_to_key

CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
HAND_ORDER = ['5', '4', 'F', '3', 'P', '2', '1']

with open('07_input', 'r') as f:
    lines = f.readlines()

hands = []

for l in lines:
    cl = l.strip()
    x, y = cl.split()
    hands.append((x, int(y)))

def card_compare(a, b):
    pos_a = CARD_ORDER.index(a)
    pos_b = CARD_ORDER.index(b)
    return pos_a - pos_b

def get_hand_type(a):
    counter = Counter(list(a))

    if len(counter) == 1:
        return '5'
    if len(counter) == 2:
        if 4 in counter.values():
            return '4'
        else:
            return 'F'
    if len(counter) == 3:
        if 3 in counter.values():
            return '3'
        else:
            return 'P'
    if len(counter) == 4:
        return '2'
    return '1'

def compare_hands(a, b):
    rank_a = get_hand_type(a)
    rank_b = get_hand_type(b)
    pos_a = HAND_ORDER.index(rank_a)
    pos_b = HAND_ORDER.index(rank_b)

    if pos_a != pos_b:
        return pos_a - pos_b

    for x, y in zip(list(a), list(b)):
        diff = card_compare(x, y)
        if diff != 0:
            return diff

    return 0

def compare_wrapper(a, b):
    return compare_hands(a[0], b[0])

sorted_hands = sorted(hands, key=cmp_to_key(compare_wrapper), reverse=True)

total = 0
for i, hand in enumerate(sorted_hands):
    total += ((i + 1) * hand[1])

print(total)
