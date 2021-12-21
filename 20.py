from collections import defaultdict

pix_map = None
max_x = 0
max_y = 0
min_x = 0
min_y = 0
grid = defaultdict(lambda:False)

def printg(grid, min_x, min_y, max_x, max_y):
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            print('#' if grid[(x,y)] else '.', end='')
        print('')

with open("20.txt") as f:
    pix_map = [x == '#' for x in f.readline().strip()]

    f.readline()

    y = 0
    for line in (l.strip() for l in f.readlines()):
        x = 0
        for c in line:
            grid[(x,y)] = c == '#'
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            x += 1
        y += 1

def apply(grid, ng, min_x, min_y, max_x, max_y):
    adjmap = [ (-1, -1), (0, -1), (1, -1), (-1, 0), (0,0), (1,0), (-1, 1), (0,1), (1,1) ]

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            bits = ''
            for a in adjmap:
                if grid[(x+a[0], y+a[1])]:
                    bits += '1'
                else:
                    bits += '0'
            num = int(bits, 2)
            new_pix = pix_map[num]
            ng[(x,y)] = new_pix

#print(pix_map)
            
#printg(grid, min_x, min_y, max_x, max_y)

g1 = grid
for i in range(0, 2):
    g2 = defaultdict(lambda:True) if i % 2 == 0 else defaultdict(lambda:False) 
    apply(g1, g2, min_x, min_y, max_x, max_y)
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    g1 = g2

#printg(ng2, min_x, min_y, max_x, max_y)
s = sum((1 if x == True else 0 for x in g1.values()))
print('part1', s)

g1 = grid
for i in range(0, 50):
    g2 = defaultdict(lambda:True) if i % 2 == 0 else defaultdict(lambda:False) 
    apply(g1, g2, min_x, min_y, max_x, max_y)
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    g1 = g2

s = sum((1 if x == True else 0 for x in g1.values()))
print('part2', s)