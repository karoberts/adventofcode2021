from typing import Collection, DefaultDict


from collections import defaultdict

signals = []
outputs = []

# 1 == 2
# 4 == 4
# 7 == 3
# 8 == 7

with open("8.txt") as f:
    for line in f.readlines():
        parts = line.strip().split(' | ')

        signals.append(parts[0].split(' '))
        outputs.append(parts[1].split(' '))

counts = defaultdict(lambda:0)

print(outputs)

for os in outputs:
    for o in os:
        counts[len(o)] += 1

print('part1', counts[2] + counts[4] + counts[3] + counts[7])