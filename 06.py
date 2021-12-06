
with open("6.txt") as f:
    fish = [int(x) for x in f.readline().strip().split(',')]
fish = [int(x) for x in '3,4,3,1,2'.split(',')]

for day in range(0, 80):
    new_fish = []
    for f in fish:
        if f == 0:
            new_fish.append(8)
            f = 7

        new_f = f - 1
        new_fish.append(new_f)

    fish = new_fish

print('part1', len(fish))