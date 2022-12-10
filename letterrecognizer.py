
from collections import defaultdict
from typing import DefaultDict


def recognize_letter(grid:dict[(tuple), bool]) -> str:
    mapping = {
        'A': {
            0: {  1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,1,2,3},
            4: {0,    3},
            5: {0,    3}
        },
        'B': {
            0: {0,1,2},
            1: {0,    3},
            2: {0,1,2},
            3: {0,    3},
            4: {0,    3},
            5: {0,1,2}
        },
        'C': {
            0: {  1,2},
            1: {0,    3},
            2: {0},
            3: {0},
            4: {0,    3},
            5: {  1, 2}
        },
        'D': {
            0: {0,1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,    3},
            4: {0,    3},
            5: {0,1,2}
        },
        'E': {
            0: {0,1,2,3},
            1: {0},
            2: {0,1,2},
            3: {0},
            4: {0},
            5: {0,1,2,3}
        },
        'F': {
            0: {0,1,2,3},
            1: {0},
            2: {0,1,2},
            3: {0},
            4: {0},
            5: {0}
        },
        'G': {
            0: {  1,2},
            1: {0,    3},
            2: {0},
            3: {0,  2,3},
            4: {0,    3},
            5: {  1,2,3}
        },
        'H': {
            0: {0,    3},
            1: {0,    3},
            2: {0,1,2,3},
            3: {0,    3},
            4: {0,    3},
            5: {0,    3}
        },
        'I': {
            0: {0,1,2},
            1: {  1},
            2: {  1},
            3: {  1},
            4: {  1},
            5: {0,1,2}
        },
        'J': {
            0: {    2,3},
            1: {      3},
            2: {      3},
            3: {      3},
            4: {0,    3},
            5: {  1,2}
        },
        'K': {
            0: {0,    3},
            1: {0,  2},
            2: {0,1},
            3: {0,  2},
            4: {0,  2},
            5: {0,    3}
        },
        'L': {
            0: {0},
            1: {0},
            2: {0},
            3: {0},
            4: {0},
            5: {0,1,2,3}
        },
        'M': {  # not sure about this one
            0: {0,    3},   
            1: {0,1,2,3},
            2: {0,1,2,3},
            3: {0,    3},
            4: {0,    3},
            5: {0,    3}
        },
        'N': {  
            0: {0,    3},   
            1: {0,1,  3},
            2: {0,1,  3},
            3: {0,  2,3},
            4: {0,  2,3},
            5: {0,    3}
        },
        'O': {  
            0: {  1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,    3},
            4: {0,    3},
            5: {  1,2}
        },
        'P': {  
            0: {0,1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,1,2},
            4: {0},
            5: {0}
        },
        'Q': {  
            0: {0,1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,    3},
            4: {0,  2,3},
            5: {  1,2,3}
        },
        'R': {  
            0: {0,1,2},
            1: {0,    3},
            2: {0,    3},
            3: {0,1,2},
            4: {0,  2},
            5: {0,    3}
        },
        'S': {  
            0: {  1,2},
            1: {0,    3},
            2: {  1},
            3: {    2},
            4: {0,    3},
            5: {  1,2}
        },
        'T': {  # not sure
            0: {0,1,2},
            1: {  1},
            2: {  1},
            3: {  1},
            4: {  1},
            5: {  1}
        },
        'U': {  
            0: {0,    3},
            1: {0,    3},
            2: {0,    3},
            3: {0,    3},
            4: {0,    3},
            5: {  1,2}
        },
        # V indistinguishable from U
        'W': {  # not sure, probably isn't used
            0: {0,    3},
            1: {0,    3},
            2: {0,  2,3},
            3: {0,  2,3},
            4: {0,  2,3},
            5: {  1,2}
        },
        'X': {
            0: {0,    3},
            1: {0,    3},
            2: {  1,2},
            3: {  1,2},
            4: {0,    3},
            5: {0,    3}
        },
        'Y': { # not sure
            0: {0,  2},
            1: {0,  2},
            2: {  1,},
            3: {  1,},
            4: {  1},
            5: {  1}
        },
        'Z': {  
            0: {0,1,2,3},
            1: {      3},
            2: {    2},
            3: {  1},
            4: {0},
            5: {0,1,2,3}
        }
    }

    for letter, m in mapping.items():
        fail = False
        #print('looking at', letter)
        for y in range(0, 6):
            row = m[y]
            for x in range(0, 4):
                #print((x,y), row, 'r', x in row, 'g', grid[(x,y)])
                if (x in row) != grid[(x,y)]:
                    #print('fail')
                    fail = True
                    break
            if fail:
                break
        if not fail:
            return letter

    print()
    for y in range(0, 6):
        for x in range(0, 6):
            if grid[(x,y)]:
                print('\u2588' * 2, end='')
            else:
                print('  ', end='')
        print()

    raise Exception('unrecognized letter')

if __name__ == '__main__':
    grid = defaultdict(lambda:False)
    grid[(1,0)] = True
    grid[(2,0)] = True
    grid[(0,1)] = True
    grid[(3,1)] = True
    grid[(0,2)] = True
    grid[(3,2)] = True
    grid[(0,3)] = True
    grid[(1,3)] = True
    grid[(2,3)] = True
    grid[(3,3)] = True
    grid[(0,4)] = True
    grid[(3,4)] = True
    grid[(0,5)] = True
    grid[(3,5)] = True

    print(recognize_letter(grid))