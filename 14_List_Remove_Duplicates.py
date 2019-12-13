# Import randint method from random module
from random import randint

# Sample list with numbers
a = [1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 9]


# Method 1
def remove_duplicates(numbers):
    '''Returns list of unique values'''
    # For each number in numbers list
    for n in numbers:
        # If this number appears more than once on the list
        if numbers.count(n) > 1:
            # Remove duplicates from numbers list
            for x in range(1, numbers.count(n)):
                numbers.remove(n)
    return numbers

# Method 2
# Sets in python has no duplicate elements,
# so we can use sets to remove duplicates
# def remove_duplicates(numbers):
#     '''Returns list of unique values'''
#     return list(set(numbers))

# Print the results
print(remove_duplicates(a))
