
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

vars = {'w':0, 'x':0, 'y':0, 'z':0}

inq = [int(c) for c in reversed('13579246899999')]

def val(v, vs):
    if isinstance(v, str):
        return vs[v]
    else:
        return v

for p in prog:
    #print(p)
    if p[0] == 'inp':
        vars[p[1]] = inq.pop()
    elif p[0] == 'add':
        vars[p[1]] += val(p[2], vars)
    elif p[0] == 'mul':
        vars[p[1]] *= val(p[2], vars)
    elif p[0] == 'div':
        vars[p[1]] //= val(p[2], vars)
    elif p[0] == 'mod':
        vars[p[1]] %= val(p[2], vars)
    elif p[0] == 'eql':
        vars[p[1]] = 1 if vars[p[1]] == val(p[2], vars) else 0

#print(vars)
#quit()

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


"""