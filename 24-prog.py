import sys
x = y = z = w = 0
inq = [int(c) for c in reversed(sys.argv[1])]
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 11
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 6
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 13
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 14
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 15
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 14
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -8
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 10
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 13
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 9
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 15
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 12
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -11
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 8
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -4
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 13
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -15
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 12
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 14
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 6
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 1
x += 14
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 9
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -1
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 15
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -8
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 4
y *= x
z += y
w = inq.pop()
x *= 0
x += z
x %= 26
z //= 26
x += -14
x = 1 if x == w else 0
x = 1 if x == 0 else 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 10
y *= x
z += y
print(x, y, z, w)
