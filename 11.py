from collections import defaultdict
from math import prod

def printg(grid, mx, my):
    for y in range(0, mx + 1):
        for x in range(0, my + 1):
           if grid[(x, y)] == 0:
               print('.', end='')
           else:
               print(grid[(x, y)], end='')
        print('')

grid = defaultdict(lambda:-1)

max_x = 0
max_y = 0
with open('11.txt') as f:
    y = 0
    for line in (x.strip() for x in f.readlines()):
        x = 0
        for c in line:
            grid[(x,y)] = int(c)
            x += 1
        y += 1
    max_y = y - 1
    max_x = x - 1

adjmap = [ (-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1) ]

flashes = 0

for step in range(0, 1000):

    #printg(grid, max_x, max_y)
    #input()

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            grid[(x,y)] += 1

    flashed = set()
    while True:
        flashed_this_round = 0
        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                coord = (x,y)
                v = grid[coord]

                if coord not in flashed and v > 9:
                    flashed.add(coord)
                    flashed_this_round += 1
                    flashes += 1

                    for a in adjmap:
                        nc = (x+a[0], y+a[1])
                        grid[nc] += 1

        if flashed_this_round == 0:
            break

    for c in flashed:
        grid[c] = 0

    if step == 100:
        print('part1', flashes)

    any_non_zero = False
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if grid[(x,y)] != 0:
                any_non_zero = True
        if any_non_zero:
            break

    if not any_non_zero:
        print('part1', step + 1)
        break
