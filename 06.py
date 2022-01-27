from collections import defaultdict

with open("6.txt") as f:
    fish = [int(x) for x in f.readline().strip().split(',')]
#fish = [int(x) for x in '3,4,3,1,2'.split(',')]

counts = defaultdict(lambda:0)

for f in fish:
    counts[f] += 1
counts[6] = 0
counts[7] = 0
counts[8] = 0

totfish = len(fish)

for day in range(0, 256):
    zeros = counts[0]
    for i in range(0, 8):
        counts[i] = counts[i+1]
    counts[6] += zeros
    counts[8] = zeros

    if day == 79:
        print('part1', sum(counts.values()))

print('part2', sum(counts.values()))