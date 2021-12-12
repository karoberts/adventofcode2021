from collections import defaultdict

cxns = defaultdict(lambda:set())

with open("12.txt") as f:
    for line in f.readlines():
        nodes = line.strip().split('-')
        cxns[nodes[0]].add(nodes[1])
        cxns[nodes[1]].add(nodes[0])

def count_paths(node, cs, visited):
    paths = 0
    for next in cs[node]:
        if next == 'start':
            continue
        if next == 'end':
            paths += 1
            continue
        if not next.isupper() and next in visited:
            continue

        n_visited = set(visited)
        n_visited.add(next)
        paths += count_paths(next, cs, n_visited)

    return paths

cur = 'start'
visited = set()
visited.add(cur)
paths = count_paths(cur, cxns, visited)
print('part1', paths)

def count_paths2(node, cs, visited, little2cave, little2cave_ct, curpath, uniq):
    paths = 0
    for next in cs[node]:
        if next == 'start':
            continue
        if next == 'end':
            pathstr = ','.join(curpath + ['end'])
            if pathstr not in uniq:
                #print(littlecave, little2cave_ct, pathstr)
                paths += 1
                uniq.add(pathstr)
            continue
        if next == little2cave:
            if little2cave_ct >= 2:
                continue
        elif not next.isupper() and next in visited:
            continue

        n_visited = set(visited)
        n_visited.add(next)
        n_cp = list(curpath)
        n_cp.append(next)
        paths += count_paths2(next, cs, n_visited, little2cave, little2cave_ct + (1 if next == little2cave else 0), n_cp, uniq)

    return paths

paths = 0
uniq = set()
for littlecave in (c for c in cxns.keys() if not c.isupper() and c != 'start' and c != 'end'):
    cur = 'start'
    visited = set()
    visited.add(cur)
    paths += count_paths2(cur, cxns, visited, littlecave, 0, ['start'], uniq)
print('part2', paths)