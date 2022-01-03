# test
#p1 = 4
#p2 = 8

# real
p1 = 2
p2 = 1


p1_score = 0
p2_score = 0

d = 1
rolls = 0

memo = dict()

seq1 = [p1]
seq2 = [p2]

dice_rolls = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}
last_double = None

def find(seq1, seq2, roll, p1):
    global dice_rolls, last_double

    if len(seq1) == 5 and last_double != str(seq1):
        memo.clear()
        last_double = str(seq1)

    def nx(c, r):
        return (c + r - 1) % 10 + 1

    if roll < 0:
        k = str(seq1) + '|' + str(seq2)
        if k in memo:
            return memo[k]

        if sum(seq1) - seq1[0] >= 21:
            return (1, 0)
        if sum(seq2) - seq2[0] >= 21:
            return (0, 1)

        ws = [0, 0]
        for amt, nu in dice_rolls.items():
            w = find(seq1, seq2, amt, p1)
            ws[0] += w[0] * nu
            ws[1] += w[1] * nu

        return ws
    else:
        if p1:
            n1 = seq1 + [nx(seq1[-1], roll)]
            k = str(n1) + '|' + str(seq2)
            r = memo[k] = find(n1, seq2, -1, not p1)
        else:
            n2 = seq2 + [nx(seq2[-1], roll)]
            k = str(seq1) + '|' + str(n2)
            r = memo[k] = find(seq1, n2, -1, not p1)
        #if r[0] > 1000000000000 or r[1] > 1000000000000:
        #   print('memo', k, r)
        return r

r = find(seq1, seq2, -1, True)

print('part2', max(r[0], r[1]))