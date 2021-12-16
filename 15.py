import heapq
from collections import defaultdict

# me = (x,y), tgt = (x,y), grid, _max=(max_x, max_y)
def dijkstra(me, tgt, grid, _max):
    I_COST = 0
    I_X = 1
    I_Y = 2
    I_KEY = 3
    I_VALID = 4

    def get_neighbors(x,y):
        tests = [ (1, 0), (-1, 0), (0, -1), (0, 1) ]
        ns = []

        for t in tests:
            test_x = x + t[0]
            test_y = y + t[1]
            if test_x < 0 or test_y < 0 or test_x > _max[0] or test_y > _max[1]:
                continue
            test_key = (test_x, test_y)

            # [ cost, x, y, key ]
            ns.append( [grid[test_key], test_x, test_y, test_key] )

        for n in ns:
            n.append(True)
        return ns

    dist = defaultdict(lambda:999999999)
    dist[me] = 0
    prev = {me: None}

    h = []
    heapq.heappush(h, [dist[me], me[0], me[1], me, True])
    finder = {me: h[0]}
    inq = set()
    inq.add(me)

    while len(h) > 0:
        u = heapq.heappop(h)
        if not u[I_VALID]:
            continue
        inq.remove(u[I_KEY])
        if u[I_X] == tgt[0] and u[I_Y] == tgt[1]:
            return u[I_COST]
        uk = u[I_KEY]
        for v in get_neighbors(u[I_X], u[I_Y]):
            alt = dist[uk] + v[I_COST]
            if alt < dist[v[I_KEY]]:
                dist[v[I_KEY]] = alt
                prev[v[I_KEY]] = (uk, v[I_COST], v[I_X], v[I_Y])
                entry = [alt, v[I_X], v[I_Y], v[I_KEY], True]
                if v[I_KEY] in inq:
                    finder[v[I_KEY]][I_VALID] = False
                inq.add(v[I_KEY])
                finder[v[I_KEY]] = entry

                heapq.heappush(h, entry)

    return dist[tgt]

def printg(grid, mx, my):
    for y in range(0, my + 1):
        for x in range(0, mx + 1):
            print(grid[(x,y)], end='')
        print('')

grid = defaultdict(lambda:0)
folds = []

max_x = 0
max_y = 0
with open('15.txt') as f:
    mode = 1
    y = 0
    for line in (l.strip() for l in f.readlines()):
        x = 0
        for c in line:
            grid[(x,y)] = int(c)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            x += 1
        y += 1

#printg(grid, max_x, max_y)

cost = dijkstra((0,0), (max_x, max_y), grid, (max_x, max_y))
print('part1', cost)

for iy in range(0, 5):
    for ix in range(0, 5):
        if ix == 0 and iy == 0:
            continue
        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                cur_v = grid[(x,y)]
                n_v = cur_v + ix + iy
                if n_v > 9:
                    n_v -= 9
                grid[(x + ix * (max_x + 1), y + iy * (max_y + 1))] = n_v

nmax_x = (max_x + 1) * 5 - 1
nmax_y = (max_y + 1) * 5 - 1
#printg(grid, nmax_x, nmax_y)

cost = dijkstra((0,0), (nmax_x, nmax_y), grid, (nmax_x, nmax_y))
print('part2', cost)