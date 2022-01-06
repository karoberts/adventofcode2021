import math
from collections import defaultdict
from typing import NewType

scanners = []

with open("19.txt") as f:
    cur_scanner = None
    for line in f.readlines():
        line = line.strip()
        if line == '':
            pass
        elif line.startswith('---'):
            cur_scanner = []
            scanners.append(cur_scanner)
        else:
            sp = [int(x) for x in line.split(',')]
            cur_scanner.append((sp[0], sp[1], sp[2]))

#print(scanners)

X = 0
Y = 1
Z = 2

# cos 90 = 0
# cos 180 = -1
# cos 270 = 0
# cos 360 = 1

# sin 90 = 1
# sin 180 = 0
# sin 270 = -1
# sin 360 = 0

mycos = {0:1, 90:0, 180:-1, 270:0}
mysin = {0:0, 90:1, 180:0, 270:-1}
def rotate(pt, pitch, roll, yaw):
    cosa = mycos[yaw]
    sina = mysin[yaw]

    cosb = mycos[pitch]
    sinb = mysin[pitch]

    cosc = mycos[roll]
    sinc = mysin[roll]

    Axx = cosa*cosb
    Axy = cosa*sinb*sinc - sina*cosc
    Axz = cosa*sinb*cosc + sina*sinc

    Ayx = sina*cosb
    Ayy = sina*sinb*sinc + cosa*cosc
    Ayz = sina*sinb*cosc - cosa*sinc

    Azx = -sinb
    Azy = cosb*sinc
    Azz = cosb*cosc

    return (Axx*pt[X] + Axy*pt[Y] + Axz*pt[Z], Ayx*pt[X] + Ayy*pt[Y] + Ayz*pt[Z], Azx*pt[X] + Azy*pt[Y] + Azz*pt[Z])

xforms = []
for p in [0, 90, 180, 270]:
    for r in [0, 90, 180, 270]:
        for y in [0, 90, 180, 270]:
            xforms.append((p,r,y))

def apply_xforms(sN, orient):
    xf = xforms[orient]
    return [rotate(c, xf[0], xf[1], xf[2]) for c in sN]

def adjust_pt(pFrom, pTo):
    return (pFrom[X] + pTo[X], pFrom[Y] + pTo[Y], pFrom[Z] + pTo[Z])

def adjust_pts(sFrom, pTo):
    return [adjust_pt(f, pTo) for f in sFrom]

def find_match(s0, sN):
    orients = defaultdict(lambda:defaultdict(lambda:[]))

    for orient in range(0, len(xforms)):
        nsN = apply_xforms(sN, orient)
        hold = []
        for i0 in range(0, len(s0)):
            c0 = s0[i0]
            for iN in range(0, len(sN)):
                cN = nsN[iN]
                x0 = c0[X]
                xN = cN[X]
                y0 = c0[Y]
                yN = cN[Y]
                z0 = c0[Z]
                zN = cN[Z]
                if x0 < 0 and xN < 0: sX = x0 + abs(xN)
                if x0 < 0 and xN >= 0: sX = -1 * (abs(x0) + xN)
                if x0 > 0 and xN < 0: sX = x0 + abs(xN)
                if x0 > 0 and xN >= 0: sX = x0 - xN

                if y0 < 0 and yN < 0: sY = y0 + abs(yN)
                if y0 < 0 and yN >= 0: sY = -1 * (abs(y0) + yN)
                if y0 > 0 and yN < 0: sY = y0 + abs(yN)
                if y0 > 0 and yN >= 0: sY = y0 - yN

                if z0 < 0 and zN < 0: sZ = z0 + abs(zN)
                if z0 < 0 and zN >= 0: sZ = -1 * (abs(z0) + zN)
                if z0 > 0 and zN < 0: sZ = z0 + abs(zN)
                if z0 > 0 and zN >= 0: sZ = z0 - zN

                #positions[(sX, sY, sZ)].append((orient, i0, iN))
                orients[orient][(sX, sY, sZ)].append((i0, iN))
                #positions[(orient, i0, iN)] = (sX, sY, sZ)
                #print(orient, i0, iN, (sX, sY, sZ), cN, (cN[X] - 20, cN[Y] - 1133, cN[Z] + 1061))

    for orient in range(0, len(xforms)):
        for k, v in orients[orient].items():
            #print(orient, k)
            if len(v) >= 12:
                #print(orient, k, v)
                return (orient, k, v)
    return None

def find_0(i, chain, path):
    for sA, sB in chain.items():
        if i in sB:
            if sA == 0:
                return path
            if sA not in path:
                p = find_0(sA, chain, path + [sA])
                if p is not None:
                    return p
        """
        if i == sA:
            for s in sB:
                if s == 0:
                    return path
                if s not in path:
                    p = find_0(s, chain, path + [s])
                    if p is not None:
                        return p
        """
    return None

chain = defaultdict(set)
converters = dict()

for i in range(0, len(scanners)):
    for j in range(i + 1, len(scanners)):
        if i == j: continue
        r = find_match(scanners[i], scanners[j])
        if r is None: continue
        converters[(j, i)] = r
        #print(i, j, 'o=', r[0], 'sO=', r[1])
        chain[i].add(j)

        r = find_match(scanners[j], scanners[i])
        if r is None: continue
        converters[(i, j)] = r
        #print(i, j, 'o=', r[0], 'sO=', r[1])
        chain[j].add(i)

def convert_pts(sId, sPts, chain, converters, path = None):
    #if path is not None:
    #    print(f'   convert from {sId} to {path}')
    if path is None:
        path = find_0(sId, chain, [])
        #print(f'-> convert from {sId} to {path}')
    if len(path) == 0:
        cv = converters[(sId, 0)]
        xPts = apply_xforms(sPts, cv[0])
        xPts = adjust_pts(xPts, cv[1])
        return xPts

    cv = converters[(sId, path[0])]
    xPts = apply_xforms(sPts, cv[0])
    xPts = adjust_pts(xPts, cv[1])
    return convert_pts(path[0], xPts, chain, converters, path[1:])

def convert_sloc3(sId, sPts, chain, converters, path):
    #if path is not None:
    #    print(f'   convert from {sId} to {path}')
        #print(f'-> convert from {sId} to {path}')
    if len(path) == 0:
        cv = converters[(sId, 0)]
        xPts = apply_xforms(sPts, cv[0])
        xPts = adjust_pts(xPts, cv[1])
        return xPts

    cv = converters[(sId, path[0])]
    xPts = apply_xforms(sPts, cv[0])
    xPts = adjust_pts(xPts, cv[1])
    return convert_pts(path[0], xPts, chain, converters, path[1:])

found = set(scanners[0])
scanner_locs = set([(0, (0,0,0))])

for sId in range(1, len(scanners)):
    ps = convert_pts(sId, scanners[sId], chain, converters)
    found = found.union(ps)

    path = find_0(sId, chain, [])
    if len(path) == 0:
        sloc = converters[sId, 0][1]
    elif len(path) > 0:
        cv = converters[(sId, path[0])]
        sloc = convert_sloc3(path[0], [cv[1]], chain, converters, path[1:])[0]

    scanner_locs.add((sId, sloc))

#for p in sorted(found):
    #print(f'{p[X]},{p[Y]},{p[Z]}')

print('part1', len(found))

def manhat_dist(c1, c2):
    return abs(c1[X] - c2[X]) + abs(c1[Y] - c2[Y]) + abs(c1[Z] - c2[Z])

#for s in scanner_locs:
    #print(s)

max_dist = 0
for s1 in scanner_locs:
    for s2 in scanner_locs:
        max_dist = max(max_dist, manhat_dist(s1[1], s2[1]))

print('part2', max_dist)

"""

path = find_0(1, chain, [])
print(path)
print(scanners_o[1])
cv = converters[(1, 0)]
print(cv)
print('1 = ', cv[1])
print()

path = find_0(4, chain, [])
print(path)
print(scanners_o[4])
cv = converters[(4, 1)]
print(cv)
cv2 = apply_xforms([cv[1]], converters[(1, 0)][0])
print('4 = ', cv2)
cv3 = adjust_pt(cv2[0], converters[(1, 0)][1])
print('4 = ', cv3)
print()

path = find_0(3, chain, [])
print(path)
print(scanners_o[3])
cv = converters[(3, 1)]
print(cv)
cv2 = apply_xforms([cv[1]], converters[(1, 0)][0])
print('3 = ', cv2)
cv3 = adjust_pt(cv2[0], converters[(1, 0)][1])
print('3 = ', cv3)
print()

path = find_0(2, chain, [])
print(path)
print(scanners_o[2])
cv = converters[(2, 4)]
print(cv)
cv2 = apply_xforms([cv[1]], converters[(4, 1)][0])
print('2 = ', cv2)
cv2a = apply_xforms([cv2[0]], converters[(1, 0)][0])
cv3 = adjust_pt(cv2a[0], converters[(1, 0)][1])
print('2 = ', cv3)

cv_41 = converters[(4, 1)]
print(cv_41)
cv_41x = apply_xforms([cv_41[1]], converters[(1, 0)][0])

cv4 = adjust_pt(cv3, cv_41x[0])
print('2 = ', cv4)
print()

quit()

found = set(scanners[0])

for i in range(1, len(scanners)):
    path = find_0(i, chain, [])
    cur = i
    adj = scanners[i]
    pt = None
    print('s=', i, path)
    for p in path:
        cv = converters[(cur, p)]
        if pt is None: pt = cv[1]
        print('A', i, pt)
        pt = apply_xforms([pt], cv[0])[0]
        print('B', i, pt)
        pt = (pt[X] + scanners_o[cur][X], pt[Y] + scanners_o[cur][Y], pt[Z] + scanners_o[cur][Z])
        print('C', i, pt)
        cur = p

    if pt is None:
        pt = converters[(cur, 0)][1]

    print('s=', i, 'o=', pt)

quit()


print('0,1')
r = find_match(scanners[0], scanners[1])
#r = (4, (68, -1246, -43), [(0, 3), (1, 8), (3, 12), (4, 1), (5, 24), (6, 18), (7, 10), (9, 0), (12, 2), (14, 5), (19, 15), (24, 19)])
new_1 = [(x + r[1][X], y + r[1][Y], z + r[1][Z]) for (x,y,z) in apply_xforms(scanners[1], r[0])]
for i in range(0, len(new_1)):
    s1 = new_1[i]
    found.add(s1)
    #print(i, s1)

#for s in sorted(found):
    #print(f'{s[X]},{s[Y]},{s[Z]}')

print('1,4')
r = find_match(scanners[1], scanners[4])

#print('2,4')
#find_match(scanners[4], scanners[2])

#print('2,3')
quit()

matches = []

for i in range(0, len(scanners)):
    for j in range(i + 1, len(scanners)):
        r = find_match(scanners[i], scanners[j])
        matches.append((i,j,r))

tot = 0
for m in matches:
    #if len(m[2][0]) < 12: continue

    print(m[0], m[1], len(scanners[m[0]]), len(scanners[m[1]]), len(m[2][0]), len(m[2][1]))

sin(90) = 1
cos(90) = 0

Around X-axis:
X = x;
Y = - z;
Z = y;
Around Y-axis:
X = z;
Y = y;
Z = - x;
Around Z-axis:
X = - y;
Y = x;
Z = z;
"""