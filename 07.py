with open("7.txt") as f:
    crabs = [int(x) for x in f.readline().strip().split(',')]
#crabs = [16,1,2,0,4,2,7,1,2,14]

mincrab = min(crabs)
maxcrab = max(crabs)

costs = dict()
for i in range(mincrab, maxcrab+1):
    costs[i] = sum([abs(x - i) for x in crabs])

minpos = min(costs, key=costs.get)
print('part1', costs[minpos])