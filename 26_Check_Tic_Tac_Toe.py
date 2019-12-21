board = [
    [2, 2, 1],
    [1, 1, 2],
    [1, 0, 0],
]

# Get the length of given board
b_size = len(board[0])


def check_rows():
    for row in range(0, b_size):
        if board[row].count(1) == b_size or board[row].count(2) == b_size:
            return True


def check_columns():
    for column in range(0, b_size):
        col = []
        for row in range(0, b_size):
            col.append(board[row][column])
        if col.count(1) == b_size or col.count(2) == b_size:
            return True


def check_diagonals():
    diagonal1 = [board[x][x] for x in range(0, b_size)]
    diagonal2 = [board[x][len(board) - (x + 1)] for x, y in enumerate(board)]

    if diagonal1.count(1) == b_size or diagonal1.count(2) == b_size:
        return True
    elif diagonal2.count(1) == b_size or diagonal2.count(2) == b_size:
        return True


def is_game_over():
    for row in range(0, b_size):
        if board[row].count(0) > 0:
            return False
    return True


check_rows()
check_columns()
check_diagonals()
print(is_game_over())
