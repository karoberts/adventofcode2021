scanners = []

with open("19-test.txt") as f:
    cur_scanner = None
    for line in f.readlines():
        line = line.strip()
        if line == '':
            pass
        elif line.startswith('---'):
            cur_scanner = set()
            scanners.append(cur_scanner)
        else:
            sp = [int(x) for x in line.split(',')]
            cur_scanner.add((sp[0], sp[1], sp[2]))

print(scanners)