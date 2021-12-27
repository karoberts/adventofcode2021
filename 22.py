import re
import math
from collections import defaultdict

instrs = []

with open("22-test-2.txt") as f:
    for line in f.readlines():
        m = re.match(r'(on|off) x=([\-\d]+)..([\-\d]+),y=([\-\d]+)..([\-\d]+),z=([\-\d]+)..([\-\d]+)', line)
        instrs.append( {'id': len(instrs) ,'on': m.group(1) == 'on', 'x': (int(m.group(2)), int(m.group(3))), 'y': (int(m.group(4)), int(m.group(5))), 'z': (int(m.group(6)), int(m.group(7)))} )

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

"""
- go through cubes
    if 'on'
        ct = volume of cube
        for each 'on' cube before:
            subtract intersection from ct
    else:
        ct -= find unique intersection between off cube and all prev 'on' cubes
"""

def uniq_counts(instrs, i):
    x = instrs[i]['x']
    y = instrs[i]['y']
    z = instrs[i]['z']
    ct = abs(x[1] - x[0]) * abs(y[1] - y[0]) * abs(z[1] - z[0])
    for j in range(i, -1, -1):
        x2 = instrs[j]['x']
        y2 = instrs[j]['y']
        z2 = instrs[j]['z']

        if x2[0] <= x[0] and x2[1] >= x[1] and y2[0] <= y[0] and y2[1] >= y[1] and z2[0] <= z[0] and z2[1] >= z[1]:
            # 2 cube entirely envelopes 1 cube
            ct = 0
            break

        if x[0] <= x2[0] and x[1] >= x2[1] and y[0] <= y2[0] and y[1] >= y2[1] and z[0] <= z2[0] and z[1] >= z2[1]:
            # 1 cube entirely envelopes 2 cube
            ct -= abs(x2[1] - x2[0]) * abs(y2[1] - y2[0]) * abs(z2[1] - z2[0])
            continue

        if x2[0] >= x[0] or x2[1] <= x[1] or y2[0] >= y[0] or y2[1] <= y[1] or z2[0] >= z[0] or z2[1] >= z[1]:
            pass
    return ct

cts = 0
for i in range(0, len(instrs)):
    for j in range(0, len(instrs)):
        if i == j: continue
        cts += uniq_counts(instrs, i)

