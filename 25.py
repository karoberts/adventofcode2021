from collections import defaultdict

max_x = 0
max_y = 0
min_x = 0
min_y = 0
grid = defaultdict(lambda:False)

def printg(grid, min_x, min_y, max_x, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[(x,y)], end='')
        print('')

with open("25.txt") as f:
    y = 0
    for line in (l.strip() for l in f.readlines()):
        x = 0
        for c in line:
            grid[(x,y)] = c
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            x += 1
        y += 1

for step in range(0, 1000):
    #print('step', step)
    #printg(grid, min_x, min_y, max_x, max_y)
    east_movers = set()
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[(x,y)] != '>':
                continue
            east_pos = (x + 1, y) if x < max_x else (0, y)
            if grid[east_pos] == '.':
                east_movers.add(((x,y), east_pos))

    for m in east_movers:
        grid[m[0]] = '.'
        grid[m[1]] = '>'

    south_movers = set()
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[(x,y)] != 'v':
                continue
            south_pos = (x, y + 1) if y < max_y else (x, 0)
            if grid[south_pos] == '.':
                south_movers.add(((x,y), south_pos))

    for m in south_movers:
        grid[m[0]] = '.'
        grid[m[1]] = 'v'

    if len(east_movers) == 0 and len(south_movers) == 0:
        print('part1', step + 1)
        break
