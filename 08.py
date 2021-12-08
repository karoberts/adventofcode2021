from typing import Collection, DefaultDict


from collections import defaultdict

signals = []
outputs = []

# 1 == 2
# 4 == 4
# 7 == 3
# 8 == 7

with open("8.txt") as f:
    for line in f.readlines():
        parts = line.strip().split(' | ')

        signals.append(parts[0].split(' '))
        outputs.append(parts[1].split(' '))

counts = defaultdict(lambda:0)

for os in outputs:
    for o in os:
        counts[len(o)] += 1

print('part1', counts[2] + counts[4] + counts[3] + counts[7])

# 0 == 6
# 1 == 2
# 2 == 5
# 3 == 5
# 4 == 4
# 5 == 5
# 6 == 6
# 7 == 3
# 8 == 7
# 9 == 6

"""
  aaaa
 b    c  
 b    c  
  dddd   
 e    f  
 e    f  
  gggg  
"""

final_nums = []


for i in range(0, len(signals)):
    signal = signals[i]
    output = outputs[i]
    #print(i, signal, output)

    mapping = {}
    m235 = set()
    m069 = set()

    for o in output:
        if len(o) == 2: mapping[1] = set(sorted(o))
        if len(o) == 4: mapping[4] = set(sorted(o))
        if len(o) == 3: mapping[7] = set(sorted(o))
        if len(o) == 7: mapping[8] = set(sorted(o))

        if len(o) == 5: m235.add(''.join(sorted(o)))
        if len(o) == 6: m069.add(''.join(sorted(o)))
    for s in signal:
        if len(s) == 2: mapping[1] = set(sorted(s))
        if len(s) == 4: mapping[4] = set(sorted(s))
        if len(s) == 3: mapping[7] = set(sorted(s))
        if len(s) == 7: mapping[8] = set(sorted(s))

        if len(s) == 5: m235.add(''.join(sorted(s)))
        if len(s) == 6: m069.add(''.join(sorted(s)))

    m235_sets = [set(x) for x in m235]

    real_map = {}
    # output 'a' determined by delta of 7 and 1
    real_map['a'] = (mapping[7] - mapping[1]).pop()

    # can find mapping of 3 by finding which of 2,3,5 have both of 1
    ones = list(mapping[1])
    for m in list(m235_sets):
        if ones[0] in m and ones[1] in m:
            mapping[3] = m
            m235_sets.remove(m)
            break

    # can find 6 by finding 6 len that only has one of 1
    m069_sets = [set(x) for x in m069]
    for m in list(m069_sets):
        if len(m - mapping[1]) == 5:
            mapping[6] = m
            m069_sets.remove(m)
            break

    # output 'c' is the one in 1 that is not in 6
    real_map['c'] = (mapping[1] - mapping[6]).pop()

    # differentiate 2 and 5 by who has output 'c'
    m235_one = m235_sets.pop()
    m235_two = m235_sets.pop()
    if real_map['c'] in m235_one:
        mapping[2] = m235_one
        mapping[5] = m235_two
    else:
        mapping[5] = m235_one
        mapping[2] = m235_two

    # differentiate between 9 and 0 by who when taking away 3, has one left
    m069_one = m069_sets.pop()
    m069_two = m069_sets.pop()
    if len(m069_one - mapping[3]) == 1:
        mapping[9] = m069_one
        mapping[0] = m069_two
    else:
        mapping[0] = m069_one
        mapping[9] = m069_two

    #print('real', real_map#)
    #print(len(mapping))
    #print('mapping', {k:''.join(sorted(v)) for k,v in mapping.items()})

    nums = []

    for o in output:
        for k,v in mapping.items():
            if set(o) == v:
                nums.append(k)

    fac = pow(10, len(nums) - 1)
    num = 0
    for n in nums:
        num += n * fac
        fac //= 10

    #print('num', num)
    final_nums.append(num)

#print(final_nums)
print('part2', sum(final_nums))