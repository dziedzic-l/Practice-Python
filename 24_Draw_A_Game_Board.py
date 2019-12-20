def draw_row(n=3):
    print(' --- ' * n)


def draw_column(n=3):
    print('|   |' * n)


def draw_board(size=3):
    for x in range(0, size):
        draw_row(size)
        draw_column(size)
    draw_row(size)


while True:
    size = int(input('Enter the size of game board: '))

    if size >= 3:
        break
    else:
        print('The game board size must have a minimum of 3 units')

draw_board(size)
