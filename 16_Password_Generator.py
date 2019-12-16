from random import randint, choice


def generate_password(strong=True):
    '''Returns generated password'''
    # Check what type of password the user has chosen
    if strong is True:
        password = ''

        # Generated passwords will be 10 characters long
        for x in range(0, 10):
            # Return character by unicode code point of character
            # and concatenate it to the string stored
            # in password variable
            password += chr(randint(32, 126))

        return password
    else:
        # List of weak passwords
        weak_passwords = [
            '123456',
            'qwerty',
            'monkey',
            'welcome',
            'princess',
            'password',
        ]

        return choice(weak_passwords)


# password variable that will store generated password
password = ''

while True:
    # Get the answer from the user
    answer = input('Do You want strong password? Type "yes" or "no": ')

    if answer == 'yes':
        password = generate_password()
        break
    elif answer == 'no':
        password = generate_password(strong=False)
        break
    else:
        print('Unknown answer')
        continue

print(f'Generated password: {password}')
