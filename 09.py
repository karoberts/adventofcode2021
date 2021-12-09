from collections import defaultdict

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

for y in range(0, max_y + 1):
    for x in range(0, max_x + 1):
        v = grid[(x,y)]
        c = 0
        for a in adjmap:
            if v < grid[(x+a[0], y+a[1])]:
                c += 1
        if c == 4:
            low_pts.append(v)

print('part1', sum((x + 1 for x in low_pts)))