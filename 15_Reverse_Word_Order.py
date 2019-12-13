# Method 1
def reverse_word_order_1(text):
    '''Returns string with reversed word order'''
    # Split a string into a list where each word is a list item
    words = text.split(' ')

    # The join() method takes all items in an iterable
    # and joins them into one string
    return ' '.join(words[::-1])


# Method 2
def reverse_word_order_2(text):
    '''Returns string with reversed word order'''
    reversed_words = []
    words = text.split(' ')

    # For each word position in text
    # Example:
    #   0     1         2        3      4  
    # | I | like | programming | in | Python
    #  -5    -4        -3        -2    -1
    #                                   ↑
    #                             We start here
    for word_position in range(-1, -len(words) - 1, -1):
        # Make list of words in reversed order
        reversed_words.append(words[word_position])

    return ' '.join(reversed_words)


text = ''

# While text variable is empty
while text.strip() == '':
    # Get the text typed by the user
    text = input('Type something... ')

# Print the results
print(reverse_word_order_1(text))
print(reverse_word_order_2(text))
