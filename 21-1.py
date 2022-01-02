# test
p1 = 4
p2 = 8

# real
p1 = 2
p2 = 1


p1_score = 0
p2_score = 0

d = 1
rolls = 0

while True:
    p1_d = d + d + 1 + d + 2
    d += 3
    rolls += 3
    p1 += p1_d
    while p1 > 10:
        p1 -= 10
    p1_score += p1

    if p1_score >= 1000:
        winner = 1
        break

    p2_d = d + d + 1 + d + 2
    d += 3
    rolls += 3
    p2 += p2_d
    while p2 > 10:
        p2 -= 10
    p2_score += p2

    if p2_score >= 1000:
        winner = 2
        break

print('part1', rolls * (p1_score if winner == 2 else p2_score))