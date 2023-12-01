#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

total = 0

word_digits = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

for l in lines:
    first = None
    last = None

    cl = l.strip()

    for i in range(len(cl)):
        if l[i].isdigit():
            if first is None:
                first = cl[i]
            last = cl[i]
        else:
            for k, v in word_digits.items():
                if cl[i:].startswith(k):
                    if first is None:
                        first = v
                    last = v

    num = int(first + last)
    total += num

print(total)
