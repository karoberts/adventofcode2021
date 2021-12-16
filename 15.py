import heapq
from collections import defaultdict

# me = (x,y), tgt = (x,y), grid, _max=(max_x, max_y)
def dijkstra(me, tgt, grid, _max):
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
        if not u[4]:
            continue
        inq.remove(u[3])
        if u[1] == tgt[0] and u[2] == tgt[1]:
            return u[0]
        uk = u[3]
        for v in get_neighbors(u[1], u[2]):
            alt = dist[uk] + v[0]
            if alt < dist[v[3]]:
                dist[v[3]] = alt
                prev[v[3]] = (uk, v[0], v[1], v[2])
                entry = [alt, v[1], v[2], v[3], True]
                if v[3] in inq:
                    finder[v[3]][4] = False
                inq.add(v[3])
                finder[v[3]] = entry

                heapq.heappush(h, entry)

    return dist[tgt]

def printg(grid, mx, my):
    for y in range(0, my + 1):
        for x in range(0, mx + 1):
            print(grid[(x,y)], end='')
        print('')

grid = defaultdict(lambda:False)
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