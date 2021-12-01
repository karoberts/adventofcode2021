from collections import defaultdict

with open("1.txt") as f:
    depths = [int(x) for x in f.readlines()]
    #depths = [199,200,208,210,200,207,240,269,260,263]

    incs = 0
    last = 99999999999
    for d in depths:
        if d > last:
            incs += 1
        last = d

    print('part1', incs)

    windows = defaultdict(lambda : 0)
    cur_win = 0
    for d in depths:
        windows[cur_win] += d
        if cur_win - 1 >= 0:
            windows[cur_win - 1] += d
            if cur_win - 2 >= 0:
                windows[cur_win - 2] += d
        cur_win += 1

    incs = 0
    last = 999999999999
    for i in range(0, len(windows) - 2):
        if windows[i] > last:
            incs += 1
        last = windows[i]

    print('part2', incs)
