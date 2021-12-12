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
