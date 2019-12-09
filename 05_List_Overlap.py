# Import randint method from random module
from random import randint

# Generate two lists of different sizes with random numbers
a = [randint(0, 10) for x in range(randint(3, 11))]
b = [randint(0, 10) for y in range(randint(3, 11))]

# Empty list that will contain common numbers between the lists
common_numbers = []

# For each number in a list
for a_element in a:
    # If number exists in b list
    if a_element in b:
        # Add number to common_numbers list
        common_numbers.append(a_element)

# Method 1
# For each number in common_numbers list
for n in common_numbers:
    # If this number appears more than once on the list
    if common_numbers.count(n) > 1:
        # Remove duplicates from common_numbers list
        for x in range(1, common_numbers.count(n)):
            common_numbers.remove(n)

# Method 2
# Sets in python has no duplicate elements,
# so we can use sets to remove duplicates
common_numbers_set = list(set(common_numbers))

# Print the results
print(common_numbers)
print(common_numbers_set)
