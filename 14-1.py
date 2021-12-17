from collections import Counter

rules = dict()
p = None

with open("14.txt") as f:
    p = f.readline().strip()
    f.readline()
    for line in f.readlines():
        rules[line[0:2]] = line[6]

for step in range(0, 10):

    next = ''
    for i in range(0, len(p) - 1):
        pair = p[i:i+2]

        if pair in rules:
            next += p[i] + rules[pair]
        else:
            next += p[i]
    next += p[-1]
    p = next

ct = Counter(p)
most = ct.most_common(1)[0][1]
least = ct.most_common()[-1][1]

print('part1', most - least)