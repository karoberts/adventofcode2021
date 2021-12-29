import sys
x = y = z = w = 0
inq = [int(c) for c in reversed(sys.argv[1])]

# d1
w = inq.pop()
x = 1
y = w + 6
z = y

# d2
w = inq.pop()
x = 1 
y = 26
z *= y
y = w + 14
z += y

# d3
w = inq.pop()
x = 1
y = 26
z *= y
y = w + 14
z += y

# z is 5137 to 10761

#d4
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

# d5
w = inq.pop()
x = z
x %= 26
x += 13
x = 1 # if x != w else 0
y = 25
#y *= x
y += 1
z *= y
y = w + 9
#y *= x
z += y

# d6
w = inq.pop()
x = z
x %= 26
x += 15
x = 1 # if x != w else 0
y = 25
#y *= x
y += 1
z *= y
y = w + 12
#y *= x
z += y

# d7
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

# d8
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

# d9
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

# d10
w = inq.pop()
x = z % 26
x += 14
x = 1 # if x != w else 0 ?? can z be negative
y = 25
y *= x
y += 1
z *= y
y = w + 6
y *= x
z += y

# d11
w = inq.pop()
x = z % 26
x += 14
x = 1 # if x != w else 0 ?? can z be negative?
y = 25
y *= x
y += 1
z *= y
y = w + 9 # 10..19
y *= x
z += y

# d12
w = inq.pop()
x = z % 26
z //= 26 # z is 10556 .. 10582 .. 10607
x += -1 # x is 2..10
x = 1 if x != w else 0
y = 25
y *= x # x is 0
y += 1
z *= y # y is 1
y = w + 15
y *= x
z += y # 406,407

# d13
w = inq.pop()
x = z
x %= 26
z //= 26 # must make z mod 26 = 9..17, range 243..589     399 to 407, limits x to 1..
x += -8 # x is 9..17
x = 1 if x != w else 0 # x must equal w
y = 25
y *= x # x must be 0
y += 1
z *= y # y must be 1
y = w + 4
y *= x
z += y # z must end at 15..23

# d14
w = inq.pop()
x = z # z is 15..23
x %= 26
z //= 26 
x += -14 # x is 15..23
x = 1 if x != w else 0 # x must equal w
#y = 25
#y *= x
#y += 1
#z *= y
y = w + 10 # y is 11 to 19
y *= x # x = 0
z += y # z = 0 and y = 0
print(x, y, z, w)
