import re
from collections import defaultdict

instrs = []

with open("22.txt") as f:
    for line in f.readlines():
        m = re.match(r'(on|off) x=([\-\d]+)..([\-\d]+),y=([\-\d]+)..([\-\d]+),z=([\-\d]+)..([\-\d]+)', line)
        instrs.append( {'on': m.group(1) == 'on', 'x': (int(m.group(2)), int(m.group(3))), 'y': (int(m.group(4)), int(m.group(5))), 'z': (int(m.group(6)), int(m.group(7)))} )

grid = defaultdict(lambda:False)

for ir in instrs:
    if ir['z'][0] < -50 or ir['z'][1] > 50: continue
    for z in range(ir['z'][0], ir['z'][1] + 1):
        if ir['y'][0] < -50 or ir['y'][1] > 50: continue
        for y in range(ir['y'][0], ir['y'][1] + 1):
            if ir['x'][0] < -50 or ir['x'][1] > 50: continue
            for x in range(ir['x'][0], ir['x'][1] + 1):
                grid[(x,y,z)] = ir['on']

print('part1', sum((1 if x else 0 for x in grid.values())))
