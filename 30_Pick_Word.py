from random import choice


def get_word():
    words = []

    with open('scrabble.txt', 'r') as words_file:
        for word in words_file.readlines():
            words.append(word.strip())

    return choice(words)


print(get_word())
