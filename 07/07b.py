#!/usr/bin/python3

from collections import Counter
from functools import cmp_to_key

# 'J' Jokers are weakest

CARD_ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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

def get_hand_possibility(a):
    new_hand = a.replace('J','')

    if len(new_hand) == 0:
        return '5'
    elif len(new_hand) == 1:
        return '5'
    elif len(new_hand) == 2:
        if new_hand[0] != new_hand[1]:
            return '4'
        else:
            return '5'
    elif len(new_hand) == 3:
        if new_hand[0] == new_hand[1] and new_hand[1] == new_hand[2]:
            return '5'
        elif new_hand[0] == new_hand[1] or new_hand[1] == new_hand[2] or new_hand[0] == new_hand[2]:
            return '4'
        else:
            return '3'
    elif len(new_hand) == 4:
        counter = Counter(list(new_hand))
        if len(counter) == 1:
            return '5'
        elif len(counter) == 2:
            if 3 in counter.values():
                return '4'
            else:
                return 'F'
        elif len(counter) == 3:
            return '3'
        else:
            return '2'
    else:
        return get_hand_type(a)

def compare_hands(a, b):
    rank_a = get_hand_possibility(a)
    rank_b = get_hand_possibility(b)
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
