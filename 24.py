import sys
import datetime
from collections import defaultdict

def isnum(v):
    return v.isnumeric() or (v.startswith('-') and v[1:].isnumeric())

prog = []
with open('24.txt') as f:
    for line in f.readlines():
        sp = line.strip().split(' ')
        if sp[0] == 'inp':
            prog.append(('inp', sp[1], None))
        elif sp[0] == 'add':
            prog.append(('add', sp[1], int(sp[2]) if isnum(sp[2]) else sp[2]))
        elif sp[0] == 'mul':
            prog.append(('mul', sp[1], int(sp[2]) if isnum(sp[2]) else sp[2]))
        elif sp[0] == 'div':
            prog.append(('div', sp[1], int(sp[2]) if isnum(sp[2]) else sp[2]))
        elif sp[0] == 'mod':
            prog.append(('mod', sp[1], int(sp[2]) if isnum(sp[2]) else sp[2]))
        elif sp[0] == 'eql':
            prog.append(('eql', sp[1], int(sp[2]) if isnum(sp[2]) else sp[2]))

def run(n, part = None):            
    vars = {'w':0, 'x':0, 'y':0, 'z':0}

    inq = [int(c) for c in reversed(n)]

    zfac = [ 1, 2, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0 ]
    cur_zfac = 0

    def val(v, vs):
        if isinstance(v, str):
            return vs[v]
        else:
            return v

    d = -1 
    for p in prog:
        #print(p)
        if p[0] == 'inp':
            #print(vars)
            if len(inq) == 0:
                #print(n)
                return -1
            vars[p[1]] = inq.pop()
            d += 1
        elif p[0] == 'add':
            vars[p[1]] += val(p[2], vars)
        elif p[0] == 'mul':
            vars[p[1]] *= val(p[2], vars)
            if p[1] == 'z' and p[2] == 'y':
                if vars['y'] == 1:
                    cur_zfac -= 1
                else:
                    cur_zfac += 1
                if cur_zfac != zfac[d]:
                    return False
                #print(cur_zfac, zfac[d])
        elif p[0] == 'div':
            vars[p[1]] //= val(p[2], vars)
        elif p[0] == 'mod':
            vars[p[1]] %= val(p[2], vars)
        elif p[0] == 'eql':
            vars[p[1]] = 1 if vars[p[1]] == val(p[2], vars) else 0

    if vars['z'] == 0:
        print(part, n)
        return True

def find_it(part):
    if part == 'part1':
        first_start = 9
        start = 9
        end = 0
        step = -1
    else:
        first_start = 9 # lowest starts with 9, saves some time (~50 seconds starting at 1)
        start = 1
        end = 10
        step = 1

    for t in range(first_start, end, step):
        st = str(t)
        for t2 in range(start, end, step):
            st2 = st + str(t2)
            for t3 in range(start, end, step):
                st3 = st2 + str(t3)
                for t4 in range(start, end, step):
                    st4 = st3 + str(t4)
                    if run(st4) > -1:
                        continue
                    for t5 in range(start, end, step):
                        st5 = st4 + str(t5)
                        if run(st5) > -1:
                            continue
                        for t6 in range(start, end, step):
                            st6 = st5 + str(t6)
                            if run(st6) > -1:
                                continue
                            for t7 in range(start, end, step):
                                st7 = st6 + str(t7)
                                if run(st7) > -1:
                                    continue
                                for t8 in range(start, end, step):
                                    st8 = st7 + str(t8)
                                    if run(st8) > -1:
                                        continue
                                    for t9 in range(start, end, step):
                                        st9 = st8 + str(t9)
                                        if run(st9) > -1:
                                            continue
                                        for t10 in range(start, end, step):
                                            st10 = st9 + str(t10)
                                            if run(st10) > -1:
                                                continue
                                            for t11 in range(start, end, step):
                                                st11 = st10 + str(t11)
                                                if run(st11) > -1:
                                                    continue
                                                for t12 in range(start, end, step):
                                                    st12 = st11 + str(t12)
                                                    if run(st12) > -1:
                                                        continue
                                                    for t13 in range(start, end, step):
                                                        st13 = st12 + str(t13)
                                                        if run(st13) > -1:
                                                            continue
                                                        for t14 in range(start, end, step):
                                                            x = run(st13 + str(t14), part)
                                                            if x:
                                                                return

find_it('part1')
find_it('part2')
quit()

print('import sys')
print('x = y = z = w = 0')
print('inq = [int(c) for c in reversed(sys.argv[1])]')
for p in prog:
    if p[0] == 'inp':
        print(p[1], '= inq.pop()')
    elif p[0] == 'add':
        print(p[1], '+=', p[2])
    elif p[0] == 'mul':
        print(p[1], '*=', p[2])
    elif p[0] == 'div':
        print(p[1], '//=', p[2])
    elif p[0] == 'mod':
        print(p[1], '%=', p[2])
    elif p[0] == 'eql':
        print(p[1], '= 1 if', p[1], '==', p[2], 'else 0')

print('print(x, y, z, w)')

"""

z = d[0] + 6
z = z * 26
z = z + d[1] + 14
z = z * 26
z = z + d[2] + 14

z = (((d[0] + 6) * 26 + d[1] + 14) * 26) + d[2] + 14
btw 5137 and 10761

-8, 13, 15, -11, -4, -15, 14, 14, -1, -8, -14

d[03] = z % 26 must be between 9 and 17

d[04] = important
d[05] = important

d[06] = z % 26 must be between 12 and 20
d[07] = z % 26 must be between 5 and 13
d[08] = z % 26 must be between 16 and 24

d[09] = important
d[10] = important

d[11] = z % 26 must be between 2 and 10
     (z % 26) == w + 1

d[12] = z % 26 must be between 9 and 17
     (z % 26) == w + 8

d[13] = z % 26 must be between 15 and 23 
     (z % 26) == w + 14


[ ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 9, 8|9, 1 ]

z factor
[ 1, 2, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0 ]

"""