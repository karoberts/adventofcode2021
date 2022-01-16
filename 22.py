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




def cubes_intersect(c1, c2):
    a = max(c1['x'][0], c1['x'][1]) > min(c2['x'][0], c2['x'][1]) 
    b = min(c1['x'][0], c1['x'][1]) < max(c2['x'][0], c2['x'][1]) 

    c = max(c1['y'][0], c1['y'][1]) > min(c2['y'][0], c2['y'][1]) 
    d = min(c1['y'][0], c1['y'][1]) < max(c2['y'][0], c2['y'][1]) 

    e = max(c1['z'][0], c1['z'][1]) > min(c2['z'][0], c2['z'][1]) 
    f = min(c1['z'][0], c1['z'][1]) < max(c2['z'][0], c2['z'][1]) 

    return a and b and c and d and e and f

def overlapping_vol(c1, c2):
    return max(min(c2['x'][1],c1['x'][1])-max(c2['x'][0],c1['x'][0]),0) * max(min(c2['y'][1],c1['y'][1])-max(c2['y'][0],c1['y'][0]),0) * max(min(c2['z'][1],c1['z'][1])-max(c2['z'][0],c1['z'][0]),0)

def cube_vol(c):
    return abs(c['x'][0] - c['x'][1]) * abs(c['y'][0] - c['y'][1]) * abs(c['z'][0] - c['z'][1])

for c in sorted(instrs, key=lambda x:x['x'][0]):
    print(c)

quit()

on = 0
for i in range(0, len(instrs)):
    if instrs[i]['on']:
        cube = cube_vol(instrs[i])
        for j in range(i - 1, -1, -1):
            if instrs[j]['on']:
                if cubes_intersect(instrs[i], instrs[j]):
                    cube -= overlapping_vol(instrs[i], instrs[j])
        on += cube
    else:
        for j in range(i - 1, -1, -1):
            if instrs[j]['on']:
                if cubes_intersect(instrs[i], instrs[j]):
                    on -= overlapping_vol(instrs[i], instrs[j])
            else:
                pass

print('part2', on)