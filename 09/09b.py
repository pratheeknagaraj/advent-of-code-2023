#!/usr/bin/python3

with open('09_input', 'r') as f:
    lines = f.readlines()

def handle_sequence(seq):
    if all(v == 0 for v in seq):
        return 0
    else:
        new_seq = []
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1] - seq[i])
        first = handle_sequence(new_seq)
        new_first = seq[0] - first
        return new_first

values = []
for l in lines:
    seq = [int(i) for i in l.strip().split()]
    values.append(handle_sequence(seq))

print(sum(values))
