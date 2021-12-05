import re
from collections import defaultdict

def getrange(coords, id):
    if coords[0][id] >= coords[1][id]:
        return range(coords[0][id], coords[1][id] - 1, -1)
    else:
        return range(coords[0][id], coords[1][id] + 1)

def printg(grid):
    for y in range(0, 10):
        for x in range(0, 10):
           if grid[(x, y)] == 0:
               print('.', end='')
           else:
               print(grid[(x, y)], end='')
        print('')

with open("5.txt") as f:
    lines = []

    for line in f.readlines():
        m = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)', line.strip())
        lines.append( (((int(m.group(1))), int(m.group(2))),  ( (int(m.group(3))), int(m.group(4)))) )

    grid = defaultdict(lambda : 0)
    for line in lines:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            continue
        for x in getrange(line, 0):
            for y in getrange(line, 1):
                grid[(x,y)] += 1

    ct = sum( (1 if x > 1 else 0 for x in grid.values()))
    print('part1', ct)

    grid = defaultdict(lambda : 0)
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            for x in getrange(line, 0):
                for y in getrange(line, 1):
                    grid[(x,y)] += 1
        else:
            xcs = list(getrange(line, 0))
            ycs = list(getrange(line, 1))
            for p in range(0, len(xcs)):
                grid[(xcs[p], ycs[p])] += 1

    ct = sum( (1 if x > 1 else 0 for x in grid.values()))
    print('part2', ct)