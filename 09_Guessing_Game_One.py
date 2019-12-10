# import randint method from random module
from random import randint

# A variable, that stores number of tries
number_of_tries = 0
# A variable, that stores number of lifes
lifes = 3
# Get random number and store it in number_to_guess variable
number_to_guess = randint(1, 9)

print('I thought of a number between 1 and 9. Guess what number it is?')

# Create an infinite loop
while True:
    # Increment number of tries by 1
    number_of_tries += 1
    # Get the answer from user
    answer = input('Your answer: ')

    # If answer contains only digits
    if answer.isdigit():
        # Convert string to integer type
        answer = int(answer)
        if answer > number_to_guess:
            print('To high')
            lifes -= 1
        elif answer < number_to_guess:
            print('To low')
            lifes -= 1
        else:
            print(f'Correct! Number of tries: {number_of_tries}')
            break

        if lifes is 0:
            print('Game over :(')
            break
    # If answer contains only alphabetic characters
    elif answer.isalpha():
        if answer == 'exit':
            print('See you next time')
            exit()
