# Get text typed by user
text = input('Type something: ')

# Method 1
# Empty string that will store reversed text
# reversed_text = ''
#
# For each character position in text
#   0   1   2   3   4   5
# | p | y | t | h | o | n |
#  -6  -5  -4  -3  -2  -1
#                       ↑
#                  We start here

# for character_position in range(-1, -len(text) - 1, -1):
#   reversed_text += text[character_position]

# Method 2 using slice notation
reversed_text = text[::-1]

# If reversed text is the same as the text
if reversed_text == text:
    print('This string is a palindrome')
else:
    print('This string is not a palindrome')
