# test
tx = (20, 30)
ty = (-10, -5)

# real
tx = (138, 184)
ty = (-125, -71)

def sim(xv, yv):
    p = (0, 0)
    maxy = -9999
    while True:
        #print(p, xv, yv)
        p = (p[0] + xv, p[1] + yv)
        dragx = 0
        if xv > 0: dragx = -1
        if xv < 0: dragx = 1
        xv += dragx
        yv -= 1

        maxy = max(p[1], maxy)

        if p[0] >= tx[0] and p[0] <= tx[1] and p[1] >= ty[0] and p[1] <= ty[1]:
            return (p, maxy)

        if p[1] < ty[0]:
            break

    return None

maxy = 0
ct = 0
for xv in range(-125, 200):
    for yv in range(-125, 200):
        s = sim(xv, yv)
        if s is not None:
            ct += 1
            maxy = max(maxy, s[1])
            #print(maxy, xv, yv)

print('part1', maxy)
print('part2', ct)