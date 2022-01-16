# test
#p1 = 4
#p2 = 8

# real
p1 = 2
p2 = 1

memo = dict()
dice_rolls = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}

def find(p1, p2, s1, s2, player1):
    global dice_rolls

    def nx(c, r):
        return (c + r - 1) % 10 + 1

    k = f'{p1}|{p2}|{s1}|{s2}|{player1}'
    if k in memo:
        return memo[k]

    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    ws = [0, 0]
    for amt, nu in dice_rolls.items():
        if player1:
            n1 = nx(p1, amt)
            w = find(n1, p2, s1 + n1, s2, not player1)
        else:
            n2 = nx(p2, amt)
            w = find(p1, n2, s1, s2 + n2, not player1)

        ws[0] += w[0] * nu
        ws[1] += w[1] * nu

    memo[k] = ws

    return ws

r = find(p1, p2, 0, 0, True)

print('part2', max(r[0], r[1]))