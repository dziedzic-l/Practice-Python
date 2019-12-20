# A variable, that stores number of tries
number_of_tries = 0

while True:
    # Get the number from the user
    number_to_guess = abs(int(input('Enter the number from range 1 to 100: ')))

    if number_to_guess > 100 or number_to_guess == 0:
        print('You must type the number from range 1 to 100')
    else:
        break

# Create a list that stores all numbers from range 1 to 100
numbers = [x for x in range(1, 100 + 1)]

# Starting position of the first element of a given list
left = 0
# Starting position of last element of a given list
right = len(numbers) - 1

while left < right:
    # Increment number of tries by 1
    number_of_tries += 1
    # Calculate position of middle element of a given list
    middle = (left + right) // 2
    if number_to_guess > numbers[middle]:
        print('To low')
        left = middle + 1
    else:
        print('To high')
        right = middle

    # Check if the number is on the list
    if number_to_guess == numbers[left]:
        print(f'Correct! Number of tries: {number_of_tries}')
        break
