import sys
x = y = z = w = 0
inq = [int(c) for c in reversed(sys.argv[1])]

w = inq.pop()
x = 1
y = w + 6
z = y

w = inq.pop()
x = 1 
y = 26
z *= y
y = w + 14
z += y

w = inq.pop()
x = 1
y = 26
z *= y
y = w + 14
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -8
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 10
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 1
x += 13
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 9
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 1
x += 15
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 12
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -11
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 8
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -4
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 13
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -15
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 12
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 1
x += 14
x = 1 # if x != w else 0 ?? can z be negative
y = 25
y *= x
y += 1
z *= y
y = w + 6
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 1
x += 14
x = 1 # if x != w else 0 ?? can z be negative?
y = 25
y *= x
y += 1
z *= y
y = w + 9
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -1
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 15
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -8
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = w + 4
y *= x
z += y

w = inq.pop()
x = z
x %= 26
z //= 26
x += -14
x = 1 if x != w else 0
y = 25
y *= x
y += 1
z *= y
y = 0
y = w + 10
y *= x
z += y
print(x, y, z, w)
