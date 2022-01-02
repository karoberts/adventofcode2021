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

def find(seq1, seq2, rolls, p1):
    def nx(c, r):
        return (c + r - 1) % 10 + 1

    next_turn = p1

    if len(rolls) == 0:
        k = str(seq1) + '|' + str(seq2)
        if k in memo:
            return memo[k]

        if sum(seq1) - seq1[0] >= 21:
            return (1, 0)
        if sum(seq2) - seq2[0] >= 21:
            return (0, 1)
    elif len(rolls) == 3:
        next_turn = not p1

        if p1:
            n1 = seq1 + [nx(seq1[-1], sum(rolls))]
            k = str(n1) + '|' + str(seq2)
            if k in memo:
                return memo[k]
            r = find(n1, seq2, [], next_turn)
            memo[k] = r
        else:
            n2 = seq2 + [nx(seq2[-1], sum(rolls))]
            k = str(seq1) + '|' + str(n2)
            if k in memo:
                return memo[k]
            r = find(seq1, n2, [], next_turn)
            memo[k] = r
        #if r[0] > 1000000000000 or r[1] > 1000000000000:
        #   print('memo', k, r)
        return r

    w1 = find(seq1, seq2, rolls + [1], next_turn)
    w2 = find(seq1, seq2, rolls + [2], next_turn)
    w3 = find(seq1, seq2, rolls + [3], next_turn)

    return (w1[0] + w2[0] + w3[0], w1[1] + w2[1] + w3[1])

r = find(seq1, seq2, [], True)

print('part2', max(r[0], r[1]))