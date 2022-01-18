from collections import defaultdict
import heapq

main_grid = defaultdict(lambda:' ')

X = 0
Y = 1

with open("23-2.txt") as f:
    y = 0
    for line in f.readlines():
        x = 0
        for c in line:
            if c == '\n': continue
            if c in ['A', 'B', 'C', 'D', '.']:
                main_grid[(x,y)] = c
            x += 1
        y += 1

entrances = {'A': (3,1), 'B': (5,1), 'C': (7,1), 'D':(9,1)}
entrance_coords = { (3,1), (5,1), (7,1), (9,1)}
room_xs = {c[X] for c in entrances.values()}
costs = {'A': 1, 'B': 10, 'C': 100, 'D':1000}

def printg(grid):
    for y in range(0, 7):
        for x in range(0, 13):
            print(grid[(x,y)], end='')
        print('')

def can_go_to_room(grid, me):
    letter = grid[me]
    entrance = entrances[letter]
    pos1 = (entrance[X], entrance[Y] + 1)
    pos2 = (entrance[X], entrance[Y] + 2)
    pos3 = (entrance[X], entrance[Y] + 3)
    pos4 = (entrance[X], entrance[Y] + 4)

    if grid[pos4] != '.' and grid[pos4] != letter:
        return False
    if grid[pos3] != '.' and grid[pos3] != letter:
        return False
    if grid[pos2] != '.' and grid[pos2] != letter:
        return False
    if grid[pos1] != '.':
        return False

    if me[X] < entrance[X]:
        for x in range(me[X] + 1, entrance[X] + 1):
            if grid[(x,entrance[Y])] != '.':
                return False
    elif me[X] > entrance[X]:
        for x in range(me[X] - 1, entrance[X] - 1, -1):
            if grid[(x,entrance[Y])] != '.':
                return False

    return True

def find_moves(grid, me):
    letter = grid[me]
    entrance = entrances[letter]
    pos1 = (entrance[X], entrance[Y] + 1)
    pos2 = (entrance[X], entrance[Y] + 2)
    pos3 = (entrance[X], entrance[Y] + 3)
    pos4 = (entrance[X], entrance[Y] + 4)

    moves = []

    # already in the right place
    if me == pos4 or (me == pos3 and grid[pos4] == letter) or (me == pos2 and grid[pos3] == letter and grid[pos4] == letter) or (me == pos1 and grid[pos2] == letter and grid[pos3] == letter and grid[pos4] == letter):
        return moves

    # in the wrong room in lower slot, upper slot blocked
    if me[Y] == pos2[Y] and grid[(me[X], me[Y] - 1)] != '.':
        return moves
    if me[Y] == pos3[Y] and (grid[(me[X], me[Y] - 1)] != '.' or grid[(me[X], me[Y] - 2)] != '.'):
        return moves
    if me[Y] == pos4[Y] and (grid[(me[X], me[Y] - 1)] != '.' or grid[(me[X], me[Y] - 2)] != '.' or grid[(me[X], me[Y] - 3)] != '.'):
        return moves

    dist_out = 0
    if me[Y] == pos4[Y]: dist_out = 4
    if me[Y] == pos3[Y]: dist_out = 3
    if me[Y] == pos2[Y]: dist_out = 2
    if me[Y] == pos1[Y]: dist_out = 1

    if can_go_to_room(grid, me):
        dist_in = 0
        if grid[pos1] == '.':
            dist_in = 1
            rtgt = pos1
        if grid[pos2] == '.':
            dist_in = 2
            rtgt = pos2
        if grid[pos3] == '.':
            dist_in = 3
            rtgt = pos3
        if grid[pos4] == '.':
            dist_in = 4
            rtgt = pos4

        # in hallway
        if me[Y] == 1:
            moves.append((rtgt, abs(me[X] - entrance[X]) * costs[letter] + costs[letter] * dist_in))
        else:
            moves.append((rtgt, abs(me[X] - entrance[X]) * costs[letter] + costs[letter] * (dist_out + dist_in)))

        # I think there would never be a reason not to go to the room if you could
        return moves

    # in wrong room, try moving out of room
    if me[Y] == pos1[Y] or me[Y] == pos2[Y] or me[Y] == pos3[Y] or me[Y] == pos4[Y]:
        for x in range(me[X] - 1, 0, -1):
            if grid[(x, 1)] == '.':
                if x not in room_xs:
                    moves.append(((x, 1), (abs(me[X] - x) + dist_out) * costs[letter]))
            else:
                break
        for x in range(me[X] + 1, 12):
            if grid[(x, 1)] == '.':
                if x not in room_xs:
                    moves.append(((x, 1), (abs(me[X] - x) + dist_out) * costs[letter]))
            else:
                break
        
    return moves

def all_done(grid):
    for letter, coord in entrances.items():
        if grid[(coord[X], coord[Y] + 1)] != letter or grid[(coord[X], coord[Y] + 2)] != letter or grid[(coord[X], coord[Y] + 3)] != letter or grid[(coord[X], coord[Y] + 4)] != letter:
            return False
    return True

def make_key(g):
    lets = []
    for c, let in g.items():
        if let not in entrances.keys():
            continue
        lets.append((c, let))
    return str(sorted(lets, key = lambda x:x[0]))

def manhat_dist(c1, c2):
    return abs(c1[X] - c2[X]) + abs(c1[Y] - c2[Y])

def calc_dist(g):
    dist = 0
    for c, let in g.items():
        if let not in entrances.keys():
            continue
        entrance = entrances[let]
        pos1 = (entrance[X], entrance[Y] + 1)
        pos2 = (entrance[X], entrance[Y] + 2)
        pos3 = (entrance[X], entrance[Y] + 3)
        pos4 = (entrance[X], entrance[Y] + 4)
        if c[X] == entrance[X] and c[Y] > 1 and g[pos1] in ['.', let] and g[pos2] in ['.', let] and g[pos3] in ['.', let] and g[pos4] in ['.', let]:
            dist += 0
        else:
            dist += manhat_dist(pos4, c)
    return dist

# grid
def dijkstra(grid):
    I_DIST = 0
    I_COST = 1
    I_KEY = 2
    I_GRID = 3
    I_VALID = 4

    def get_neighbors(g, cost):
        ns = []
        for c, let in g.items():
            if let not in entrances.keys():
                continue
            moves = find_moves(g, c)

            for m in moves:
                # [ cost, g, key ]
                ng = g.copy()
                ng[c] = '.'
                ng[m[0]] = let
                ns.append( [calc_dist(ng), m[1] + cost, make_key(ng), ng] )
        return ns

    cost = defaultdict(lambda:999999)
    cost[make_key(grid)] = 0

    h = []
    heapq.heappush(h, [calc_dist(grid), 0, str(grid), grid, True])

    min_cost = 99999999

    while len(h) > 0:
        u = heapq.heappop(h)
        if not u[I_VALID]:
            continue
        if all_done(u[I_GRID]):
            # my heuristic isn't perfect, so it finds one solution first.  we take the second which is correct (to save time searching the whole queue)
            if u[I_COST] < min_cost and min_cost < 9999999:
                return u[I_COST]
            #if u[I_COST] < min_cost:
            #    print('min', u[I_COST])
            min_cost = min(u[I_COST], min_cost)
            continue
        uk = u[I_KEY]
        for v in get_neighbors(u[I_GRID], u[I_COST]):
            if cost[v[I_KEY]] < v[I_COST]:
                continue
            cost[v[I_KEY]] = v[I_COST] 
            heapq.heappush(h, [v[I_DIST], v[I_COST], v[I_KEY], v[I_GRID], True])

    return min_cost

#printg(main_grid)

# solves it pretty quickly, but takes about 35 seconds to find all solutions
cost = dijkstra(main_grid)

print('part2', cost)