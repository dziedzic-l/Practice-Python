from random import choice

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def get_word():
    '''Drawns the word from file'''
    words = []

    with open('scrabble.txt', 'r') as words_file:
        for word in words_file.readlines():
            words.append(word.strip())

    return choice(words)


def hide_letters(word):
    '''Hides the drawn word by replacing letter with "_" character'''
    for x in range(0, len(word)):
        # Hide random selected characters in selected word
        # by replacing them with "_" character.
        word = word.replace(word[x], "_")
    return word


while True:
    incorrect_answers = 0
    drawn_word = get_word()
    original_word = drawn_word
    drawn_word = list(hide_letters(drawn_word))
    guessed_letters = set()

    print(HANGMANPICS[incorrect_answers])

    while drawn_word.count('_') > 0 and incorrect_answers != 6:
        print(''.join(drawn_word))
        letter = input("Enter the letter: ").upper()

        # Check if typed letter has already used
        if letter[0] not in guessed_letters:
            # Check if the letter appends in the drawn word
            if original_word.count(letter[0]) > 0:
                for letter_position in range(0, len(original_word)):
                    if letter[0] == list(original_word)[letter_position]:
                        drawn_word[letter_position] = letter[0]
                        guessed_letters.add(letter[0])
            else:
                incorrect_answers += 1
                print(HANGMANPICS[incorrect_answers])
        else:
            print('This letter has already been used')

    if incorrect_answers == 6:
        print('Game over')
    elif drawn_word.count('_') == 0:
        print('Well done!')

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
