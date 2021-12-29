import math
from collections import defaultdict

scanners = []

with open("19-test.txt") as f:
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

def rotate_x(coord):
    return (coord[X], coord[Z] * -1, coord[Y])

def rotate_y(coord):
    return (coord[Z], coord[Y], coord[X] * -1)

def rotate_z(coord):
    return (coord[Y] * -1, coord[X], coord[Z])

def apply_xforms(sN, orient):
    if orient < 4:
        for i in range(0, orient):
            sN = [rotate_x(c) for c in sN]
    elif orient < 8:
        for i in range(0, orient):
            sN = [rotate_x(rotate_y(rotate_y(c))) for c in sN]
    elif orient < 12:
        for i in range(0, orient):
            sN = [rotate_y(c) for c in sN]
    elif orient < 16:
        for i in range(0, orient):
            sN = [rotate_y(rotate_x(rotate_x(c))) for c in sN]
    elif orient < 20:
        for i in range(0, orient):
            sN = [rotate_z(c) for c in sN]
    elif orient < 24:
        for i in range(0, orient):
            sN = [rotate_z(rotate_y(rotate_y(c))) for c in sN]
    return sN


def find_match(s0, sN):
    used = set()
    slns = set()
    for i in range(0, 24):
        test_coords = apply_xforms(sN, i)
        if test_coords[0] in used:
            continue
        #print(i, test_coords[0])
        used.add(test_coords[0])

        deltas = defaultdict(lambda:0)

        for j in range(0, len(test_coords)):
            c = test_coords[j]
            for c0 in s0:
                #print(c0, s0)
                for mx in range(0, 3):
                    if mx == 0: dx = abs(c[X]) - abs(c0[X])
                    elif mx == 1: dx = abs(c[X]) + abs(c0[X])
                    elif mx == 2: dx = abs(c0[X]) - abs(c[X])
                    for my in range(0, 3):
                        if my == 0: dy = abs(c[Y]) - abs(c0[Y])
                        elif my == 1: dy = abs(c[Y]) + abs(c0[Y])
                        elif my == 2: dy = abs(c0[Y]) - abs(c[Y])
                        for mz in range(0, 3):
                            if mz == 0: dz = abs(c[Z]) - abs(c0[Z])
                            elif mz == 1: dz = abs(c[Z]) + abs(c0[Z])
                            elif mz == 2: dz = abs(c0[Z]) - abs(c[Z])
                            deltas[(dx,dy,dz)] += 1
                            deltas[(-dx,-dy,-dz)] += 1

        for dd, ct in deltas.items():
            if ct >= 12:
                slns.add((i, dd))

    for s in sorted(slns, key=lambda x:x[0]):
        if s[1] == (68, -1246, -43):
            print('!', s)
        else:
            print(s)

    return None

s0 = scanners[0]
find_match(s0, scanners[1])


"""
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