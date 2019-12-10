# import choice method from random module
from random import choice

# List of available choices
choices = ['paper', 'scissors', 'rock']


def get_choice_from_player(player, choices):
    '''Returns the choice typed by the player'''
    while True:
        choice = input(f'{player}: Paper, scissors or rock?: ')
        # Check if player typed correct choice
        if choice not in choices:
            print("You must type 'paper', 'scissors' or 'rock'")
        else:
            return choice


# Print the start menu
print('''
    Choose game mode:
    1) Single player
    2) Two players
''')

# Get the menu option choosed by player
game_mode = int(input('I choose: '))

# Create an infinite loop
while True:
    # Get the choice typed by the player
    p1_choice = get_choice_from_player('Player1', choices)

    if game_mode == 1:
        # Get the choice from computer
        p2_choice = choice(choices)
        print(f'Player2 has choosen {p2_choice}')
    else:
        p2_choice = get_choice_from_player('Player2', choices)

    # Case 1 - The player's 1 choice and player's 2 choice are the same
    if p1_choice == p2_choice:
        print('Draw')
    # Case 2 - The player 1 choose paper
    elif p1_choice == 'paper':
        if p2_choice == 'scissors':
            print('Player2 wins!')
        else:
            print('Player1 win!')
    # Case 2 - The player 1 choose scissors
    elif p1_choice == 'scissors':
        if p2_choice == 'paper':
            print('Player1 win!')
        else:
            print('Player2 wins!')
    # Case 3 - The player 1 rock
    elif p1_choice == 'rock':
        if p2_choice == 'paper':
            print('Player2 wins!')
        else:
            print('Player1 win!')

    while True:
        # Ask the player if he wants to play again
        answer = input("Do You want to play again? Type 'yes' or 'no': ")

        if answer == 'yes':
            break
        elif answer == 'no':
            print('See you next time!')
            # Exit the game
            exit()
        # If the player typed something different
        else:
            print('Unknown answer, try again')
            continue
