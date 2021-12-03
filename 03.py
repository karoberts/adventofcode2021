
with open("3.txt") as f:
    nums = [x.strip() for x in f.readlines()]
    maxlen = len(max(nums, key=lambda x:len(x)))
    count = len(nums)

    one_counts = [0] * maxlen

    for num in nums:
        for j in range(0, maxlen):
            if num[j] == '1':
                one_counts[j] += 1

    #print(maxlen, count, one_counts)

    num = ''
    for i in range(0, maxlen):
        num += '1' if one_counts[i] > count // 2 else '0'

    #print(num)
    opp_num = ''.join(('1' if x == '0' else '0' for x in num))
    #print(opp_num)

    print('part1', int(num, 2) * int(opp_num, 2))