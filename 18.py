import json
import math

def parse(sfstr):
    n = []
    d = 0
    cn = None
    for c in sfstr:
        if c == '[':
            n.append('[')
        elif c == ']':
            if cn is not None:
                n.append(int(cn))
            cn = None
            n.append(']')
        elif c == ',':
            if cn is not None:
                n.append(int(cn))
            cn = None
        else:
            if cn is None:
                cn = c
            else:
                cn += c
    return n


def add(sf1, sf2):
    return ['['] + sf1 + sf2 + [']']

def reduce(sf):
    def find_right(ri):
        for ni in range(ri + 3, len(sf)):
            if isinstance(sf[ni], int):
                #print('found right', sf[ni])
                return ni
        #print('no right')
        return None

    while True:
        i = 0
        prev_num_i = None
        changed = False
        d = 0
        while i < len(sf):
            if i == len(sf):
                break
            if sf[i] is None:
                pass
            elif sf[i] == '[':
                d += 1
            elif sf[i] == ']':
                d -= 1
            elif d == 5:
                if isinstance(sf[i], int) and isinstance(sf[i+ 1], int):
                    #print('found num at 4 deep i=', i + 1, 'n=', sf[i], 'n+1=', sf[i + 1], 'prev=', prev_num_i)
                    if prev_num_i is not None:
                        sf[prev_num_i] += sf[i]
                    next_right_i = find_right(i)
                    if next_right_i is not None:
                        sf[next_right_i] += sf[i + 1]
                    sf[i] = 0
                    sf[i + 1] = None
                    sf[i - 1] = None
                    sf[i + 2] = None
                    sf = [x for x in sf if x is not None]
                    changed = True
                    break

            if isinstance(sf[i], int):
                prev_num_i = i
            i += 1
        
        if not changed:
            i = 0
            while i < len(sf):
                if i == len(sf):
                    break
                if sf[i] is None:
                    pass
                elif sf[i] == '[':
                    d += 1
                elif sf[i] == ']':
                    d -= 1

                if isinstance(sf[i], int):
                    if sf[i] >= 10:
                        #print('spltting', sf[i], 'at', i)
                        new_sf = []
                        for _i in range(0, i):
                            new_sf.append(sf[_i])
                        new_sf.append('[')
                        new_sf.append(sf[i] // 2)
                        new_sf.append(math.ceil(sf[i]/2))
                        new_sf.append(']')
                        for _i in range(i + 1, len(sf)):
                            new_sf.append(sf[_i])
                        sf = new_sf
                        changed = True
                        break
                i += 1

        #print('new sf', sf)
        if not changed:
            break

    return sf 

def magnitude(sf):
    tot_mag = 0
    d = 0
    while len(sf) > 1:
        for i in range(0, len(sf)):
            if isinstance(sf[i], int) and isinstance(sf[i+1], int):
                local_mag = sf[i] * 3 + sf[i + 1] * 2
                sf[i] = local_mag
                sf[i-1] = None
                sf[i+1] = None
                sf[i+2] = None
                sf = [x for x in sf if x is not None]
                #print(sf)
                break
    return sf[0]

with open('18.txt') as f:
    lines = [parse(x.strip()) for x in f.readlines()]

_sum = lines[0]
for i in range(1, len(lines)):
    #print('adding', _sum, lines[i])
    _sum = add(_sum, lines[i])
    _sum = reduce(_sum)
    #print('got', _sum)

print('part1', magnitude(_sum))

sums = []
for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        if i == j: continue
        _sum = add(lines[i], lines[j])
        sums.append(magnitude(reduce(_sum)))

print('part2', max(sums))
