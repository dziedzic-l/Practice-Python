board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Get the length of given board
b_size = len(board[0])


def is_available_move():
    for row in range(0, b_size):
        if board[row].count(0) > 0:
            return True
    return False


def print_board(board):
    for row in board:
        print(row)


player1 = "Player1"
player2 = "Player2"

turn = player2

while is_available_move():
    if turn == player1:
        turn = player2
    else:
        turn = player1

    while True:
        try:
            move = input(f'{turn}, enter coordinates(x, y): ')

            x, y = move.split(',')

            if board[int(x) - 1][int(y) - 1] == 0:
                if turn == player1:
                    board[int(x) - 1][int(y) - 1] = 'X'
                    break
                else:
                    board[int(x) - 1][int(y) - 1] = 'O'
                    break
            else:
                print('This field is already taken')
        except ValueError:
            print('Invalid format of coordinates.')
        except IndexError:
            print('Field coordinates are beyond the board')

    print_board(board)

print("Game over")
