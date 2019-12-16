from random import randint

# Generate four digits number to guess
number = str(randint(1000, 9999))
# Attempts number
attempts = 0

while True:
    cows = 0
    bulls = 0
    missed_digits = []
    attempts += 1

    # Get the answer typed by the user
    answer = input("Guess the number: ")

    # Check if the given answer contains 4 digits
    if not answer.isdigit() or len(answer) != 4:
        print('You must type 4 digit number')
    else:
        # For each digit position
        for digit_position in range(0, len(number)):
            # Add 1 bull if the user guessed correctly
            # in the correct place
            if answer[digit_position] == number[digit_position]:
                bulls += 1
            else:
                # Add digit from number to guess to missed_digits list
                missed_digits.append(number[digit_position])
                # If digit in number typed by the user appears
                # in missed_digits list
                if answer[digit_position] in missed_digits:
                    cows += 1
                    missed_digits.remove(answer[digit_position])
                else:
                    # Check if digit in number typed by the user
                    # appears in the rest of the number
                    for i in range(digit_position, 4):
                        if answer[digit_position] in number[i:4]:
                            cows += 1
                            break
        print("Bulls: " + str(bulls) + " Cows: " + str(cows))

        if bulls == 4:
            print("Congratulations! Attempts number: " + str(attempts))
            break
