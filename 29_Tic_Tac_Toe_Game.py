def display_broad(board):
    '''Prints the board'''
    chars = {0: " ", 1: "X", 2: "O"}

    for row in range(0, len(board)):
        print(' --- ' * len(board))
        cells = ''
        for cell in range(0, len(board)):
            cells += f'| {chars[board[row][cell]]} |'
        print(cells)
    print(' --- ' * len(board))


def check_rows(board):
    '''Checks if row has the same values'''
    for row in range(0, len(board)):
        if board[row].count(1) == len(board) or board[row].count(2) == len(board):
            return True
    return False


def check_columns(board):
    '''Checks if column has the same values'''
    for column in range(0, len(board)):
        col = []
        for row in range(0, len(board)):
            col.append(board[row][column])
        if col.count(1) == len(board) or col.count(2) == len(board):
            return True
    return False


def check_diagonals(board):
    '''Checks if diagonal of the gameboard have the same values'''
    diagonal1 = [board[x][x] for x in range(0, len(board))]
    diagonal2 = [board[x][len(board) - (x + 1)] for x, y in enumerate(board)]

    if diagonal1.count(1) == len(board) or diagonal1.count(2) == len(board):
        return True
    elif diagonal2.count(1) == len(board) or diagonal2.count(2) == len(board):
        return True
    return False


def check_board(board):
    if check_rows(board) or check_columns(board) or check_diagonals(board):
        return True
    else:
        return False


def is_available_move():
    '''Checks if there is an available move'''
    for row in range(0, len(board)):
        if board[row].count(0) > 0:
            return True
    return False


if __name__ == '__main__':
    # Get the size of the game board
    while True:
        size = int(input('Enter the size of game board: '))

        if size >= 3:
            break
        else:
            print('The game board size must have a minimum of 3 units')

    # Create game board matrix
    board = [[0] * size for x in range(0, size)]

    # Create two players
    player1 = "Player1"
    player2 = "Player2"

    turn = player1

    display_broad(board)

    while is_available_move():
        while True:
            try:
                move = input(f'{turn}, enter coordinates(x, y): ')

                x, y = move.split(',')

                if board[int(x) - 1][int(y) - 1] == 0:
                    if turn == player1:
                        board[int(x) - 1][int(y) - 1] = 1
                    else:
                        board[int(x) - 1][int(y) - 1] = 2
                    if check_board(board):
                        print(f'{turn} wins!')
                        exit()
                    else:
                        break
                else:
                    print('This field is already taken')
            except ValueError:
                print('Invalid format of coordinates.')
            except IndexError:
                print('Field coordinates are beyond the board')
            finally:
                display_broad(board)
                if turn == player1:
                    turn = player2
                else:
                    turn = player1
    print('Tie')
