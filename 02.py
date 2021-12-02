with open("2.txt") as f:
    cmds = [x for x in f.readlines()]

    cur_depth = 0
    cur_pos = 0
    for c in cmds:
        if c.startswith('forward'):
            cur_pos += int(c[len('forward') + 1:])
        elif c.startswith('up'):
            cur_depth -= int(c[len('up') + 1:])
        elif c.startswith('down'):
            cur_depth += int(c[len('down') + 1:])

    print('part1', cur_depth * cur_pos)

    cur_depth = 0
    cur_pos = 0
    cur_aim = 0
    for c in cmds:
        if c.startswith('forward'):
            x = int(c[len('forward') + 1:])
            cur_pos += x
            cur_depth += cur_aim * x
        elif c.startswith('up'):
            cur_aim -= int(c[len('up') + 1:])
        elif c.startswith('down'):
            cur_aim += int(c[len('down') + 1:])

    print('part2', cur_depth * cur_pos)