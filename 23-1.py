from collections import defaultdict
import heapq

main_grid = dict()

X = 0
Y = 1

with open("23.txt") as f:
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
    for y in range(0, 5):
        for x in range(0, 13):
            print(grid[(x,y)], end='')
        print('')

def can_go_to_room(grid, me):
    letter = grid[me]
    entrance = entrances[letter]
    pos1 = (entrance[X], entrance[Y] + 1)
    pos2 = (entrance[X], entrance[Y] + 2)

    if grid[pos1] != '.':
        return False

    if grid[pos2] != '.' and grid[pos2] != letter:
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

    moves = []

    # already in the right place
    if me == pos2 or (me == pos1 and grid[pos2] == letter):
        return moves

    # in the wrong room in lower slot, upper slot blocked
    if me[Y] == pos2[Y] and grid[(me[X], me[Y] - 1)] != '.':
        return moves

    if can_go_to_room(grid, me):
        # in hallway
        if me[Y] == 1:
            if grid[pos1] == '.':
                if grid[pos2] == '.':
                    moves.append((pos2, abs(me[X] - entrance[X]) * costs[letter] + costs[letter] * 2))
                else:
                    moves.append((pos1, abs(me[X] - entrance[X]) * costs[letter] + costs[letter]))
        else:
            dist_out = 1 if me[Y] == pos1[Y] else 2
            dist_in = 1 if grid[pos2] != '.' else 2
            tgt = pos2 if grid[pos2] == '.' else pos1
            moves.append((tgt, abs(me[X] - entrance[X]) * costs[letter] + costs[letter] * (dist_out + dist_in)))

        # I think there would never be a reason not to go to the room if you could
        return moves

    # in wrong room, try moving out of room
    if me[Y] == pos1[Y] or me[Y] == pos2[Y]:
        dist = 1 if me[Y] == pos1[Y] else 2
        for x in range(me[X] - 1, 0, -1):
            if grid[(x, 1)] == '.':
                if x not in room_xs:
                    moves.append(((x, 1), (abs(me[X] - x) + dist) * costs[letter]))
            else:
                break
        for x in range(me[X] + 1, 12):
            if grid[(x, 1)] == '.':
                if x not in room_xs:
                    moves.append(((x, 1), (abs(me[X] - x) + dist) * costs[letter]))
            else:
                break
        
    return moves

def all_done(grid):
    for letter, coord in entrances.items():
        if grid[(coord[X], coord[Y] + 1)] != letter or grid[(coord[X], coord[Y] + 2)] != letter:
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
        pos2 = (entrance[X], entrance[Y] + 1)
        if c != pos1 and c != pos2:
            dist += manhat_dist(pos1, c)
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
            # uncomment to get answer sooner
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

# solves it pretty quickly, but takes about 9 seconds to find all solutions
cost = dijkstra(main_grid)

print('part1', cost)