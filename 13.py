from collections import defaultdict
from math import prod
from letterrecognizer import recognize_letter

def printg(grid, mx, my):
    for y in range(0, my + 1):
        for x in range(0, mx + 1):
            print("\u2588" if grid[(x, y)] else '.', end='')
        print('')

grid = defaultdict(lambda:False)
folds = []

max_x = 0
max_y = 0
with open('13.txt') as f:
    mode = 1
    for line in (x.strip() for x in f.readlines()):
        if mode == 1 and len(line) == 0:
            mode = 2
            continue
        if mode == 1:
            cs = [int(d) for d in line.split(',')]
            grid[(cs[0], cs[1])] = True
            max_x = max(cs[0], max_x)
            max_y = max(cs[1], max_y)
        elif mode == 2:
            folds.append((line[len('fold along ')], int(line.split('=')[1])))

def fold_x(grid, x, mx, my):
    for y in range(0, my + 1):
        for fx in range(x + 1, mx + 1):
            #print('moving', (x,fy), 'to', (x, fy - (fy - y) * 2), 'fy=', fy)
            grid[(fx - (fx - x) * 2, y)] |= grid[(fx, y)]
            grid[(fx, y)] = False

def fold_y(grid, y, mx, my):
    #print('folding y', y)
    for fy in range(y + 1, my + 1):
        for x in range(0, mx + 1):
            #print('moving', (x,fy), 'to', (x, fy - (fy - y) * 2), 'fy=', fy)
            grid[(x, fy - (fy - y) * 2)] |= grid[(x, fy)]
            grid[(x, fy)] = False

#print(max_x, max_y)
#printg(grid, max_x, max_y)

first = True
for f in folds:
    if f[0] == 'y':
        fold_y(grid, f[1], max_x, max_y)
        max_y = f[1] + 1
    else:
        fold_x(grid, f[1], max_x, max_y)
        max_x = f[1] + 1
    if first:
        print('part1', sum((1 for c in grid.values() if c)))
        first = False

printg(grid, max_x, max_y)

grids = [defaultdict(lambda:False) for _ in range(0, 8)]

for y in range(0, max_y):
    for x in range(0, max_x):
        letter_idx = x // 5
        if letter_idx < 8:
            grids[letter_idx][(x % 5, y)] = grid[(x,y)]

print('part2 ', end='')
for g in grids:
    print(recognize_letter(g), end='')
print()
