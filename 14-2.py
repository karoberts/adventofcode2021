from collections import Counter, defaultdict
from datetime import datetime

rules = dict()
p = None

with open("14.txt") as f:
    p = f.readline().strip()
    f.readline()
    for line in f.readlines():
        rules[line[0:2]] = line[6]

memo = dict()

def recurse(start, pair, counts, depth, maxdepth):
    if depth >= maxdepth:
        #print(pair[0], 'a')
        counts[pair[0]] += 1
        return

    if (pair, depth) in memo:
        for (k, v) in memo[(pair, depth)].items():
            counts[k] += v
        return

    if pair in rules:
        #counts[pair[0]] += 1
        next_char = rules[pair]
        #print(' ' * depth * 2, pair, '=>', pair[0] + next_char + pair[1])
        orig_counts = counts.copy()
        recurse(True, pair[0] + next_char, counts, depth + 1, maxdepth)
        recurse(False, next_char + pair[1], counts, depth + 1, maxdepth)
        delta = {k:v - orig_counts[k] for (k,v) in counts.items()}
        memo[(pair, depth)] = delta

        #if not start:
        #    print(pair[1], 'b')
        #    counts[pair[1]] += 1
        #if not start:
        #    counts[pair[1]] += 1
    else:
        #print(i, p[0])
        #print(pair[0], '*')
        counts[pair[0]] += 1
        if start:
            #print(pair[1], '*')
            counts[pair[1]] += 1
        #counts[p[1]] += 1


counts = defaultdict(lambda:0)

#print('Total', len(p))
for i in range(0, len(p) - 1):
    pair = p[i:i+2]
    #print(datetime.now(), 'Run for', pair, 'at', i)
    recurse(i == 0, pair, counts, 0, 40)

counts[p[-1]] += 1
#print(p[-1])

#print(counts)
#print(sum(counts.values()))
print('part2', max(counts.values()) - min(counts.values()))