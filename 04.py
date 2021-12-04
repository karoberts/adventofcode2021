
def mark_boards(boards, marks, n):
    for i in range(0, len(boards)):
        for j in range(0, len(boards[i])):
            for k in range(0, len(boards[i][j])):
                if boards[i][j][k] == n:
                    marks[i][j][k] = 1

def check_wins(marks, boards_won):
    winners = set()
    for i in range(0, len(marks)):
        if i in boards_won:
            continue
        col_sums = [0] * 5
        for j in range(0, len(marks[i])):
            if sum(marks[i][j]) == len(marks[i][j]):
                winners.add(i)
                break
            for k in range(0, len(marks[i][j])):
                col_sums[k] += marks[i][j][k]
        if not i in winners:
            if any( (x == 5 for x in col_sums) ):
                winners.add(i)
    return winners

def sum_unmarked(board, mark):
    s = 0
    for j in range(0, len(board)):
        for k in range(0, len(board[j])):
            if mark[j][k] == 0:
                s += board[j][k]
    return s


with open("4.txt") as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]

    boards = []
    marks = []

    line_id = 0
    cur_board = None
    cur_marks = None
    for line in f.readlines():
        if line_id == 0:
            line_id += 1
            continue

        if line_id == 1:
            cur_board = []
            cur_marks = []
            boards.append(cur_board)
            marks.append(cur_marks)

        cur_board.append( [int(x) for x in line.strip().split()] )
        cur_marks.append( [0] * len(cur_board[0]) )

        line_id += 1
        if line_id == 6:
            line_id = 0        

    last_unmarked = None
    last_winner = None
    boards_won = set()
    for n in numbers:
        mark_boards(boards, marks, n)
        winners = check_wins(marks, boards_won)
        for winner in winners:
            boards_won.add(winner)
            #print('winner is board', winner, 'on num', n)
            unmarked = sum_unmarked(boards[winner], marks[winner])
            #print('unmarked', unmarked)
            if last_unmarked is None:
                print('part1', n * unmarked)
            last_unmarked = unmarked
            last_winner = n

    print('part2', last_unmarked * last_winner)