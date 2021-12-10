from collections import defaultdict
from math import prod

grid = defaultdict(lambda:99999999)

max_x = 0
max_y = 0
with open('9.txt') as f:
    y = 0
    for line in (x.strip() for x in f.readlines()):
        x = 0
        for c in line:
            grid[(x,y)] = int(c)
            x += 1
        y += 1
    max_y = y - 1
    max_x = x - 1

adjmap = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]

low_pts = []
low_pts_xy = []

for y in range(0, max_y + 1):
    for x in range(0, max_x + 1):
        v = grid[(x,y)]
        c = 0
        for a in adjmap:
            if v < grid[(x+a[0], y+a[1])]:
                c += 1
        if c == 4:
            low_pts.append(v)
            low_pts_xy.append((x,y))

print('part1', sum((x + 1 for x in low_pts)))

def find_basin(g, coord, visited):
    if coord in visited or g[coord] >= 9:
        return 0
    
    visited.add(coord)
    v = 1
    for a in adjmap:
        v += find_basin(g, (coord[0] + a[0], coord[1] + a[1]), visited)
    return v

basin_sizes = []
for lp in low_pts_xy:
    visited = set()
    basin_sizes.append(find_basin(grid, lp, visited))

print('part2', prod(list(sorted(basin_sizes, reverse=True))[:3]))
