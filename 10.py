from typing import ForwardRef


with open('10.txt') as f:
    lines = [x.strip() for x in f.readlines()]

    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_map = {'(': ')', '[': ']', '{': '}', '<': '>'}

    incomplete = []

    points = 0
    for line in lines:
        stack = []
        failed = False
        for c in line:
            if c in open_map.keys():
                stack.append(c)
            elif c in score_map:
                last = stack.pop()
                if c != open_map[last]:
                    #print(line, 'Expected', open_map[last], 'but found', c)
                    points += score_map[c]
                    failed = True
                    break
        if not failed:
            #print('line ok:', line, stack)
            incomplete.append(stack)

    print('part1', points)

    p2_score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []

    for inc in incomplete:
        score = 0
        for c in reversed(inc):
            score *= 5
            score += p2_score_map[open_map[c]]
        scores.append(score)
        
    print('part2', list(sorted(scores))[len(scores) // 2])

