
def find_bits(nums, maxlen):
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

    return (num, opp_num, one_counts)

with open("3.txt") as f:
    nums = [x.strip() for x in f.readlines()]
    maxlen = len(max(nums, key=lambda x:len(x)))
    count = len(nums)

    (num, opp_num, one_counts) = find_bits(nums, maxlen)

    print('part1', int(num, 2) * int(opp_num, 2))

    o_nums = nums
    found = []

    for b in [('1', '0'), ('0', '1')]:
        #print('start', b)
        for i in range(0, maxlen):
            #print('bit', i, 'ones', one_counts[i], 'c', count)
            oppo = count - one_counts[i]
            if one_counts[i] >= oppo:
                filter_bit = b[0]
            else:
                filter_bit = b[1]
            #print('filter', filter_bit)

            nums = [n for n in nums if n[i] == filter_bit]
            count = len(nums)

            if count == 1:
                #print('found', b[0], nums[0])
                found.append(int(nums[0], 2))
                break

            (num, opp_num, one_counts) = find_bits(nums, maxlen)
        nums = o_nums
        count = len(nums)
        (num, opp_num, one_counts) = find_bits(nums, maxlen)

    #print(found)
    print('part2', found[0] * found[1])
