# Import randint method from random module
from random import randint


def common_numbers(list1, list2):
    '''Generate set of common numbers between the lists
       and convert it to list data type'''
    return list({x for x in a for y in b if x == y})


# Generate two lists of different sizes with random numbers
a = [randint(1, 100) for x in range(5, randint(5, 30))]
b = [randint(1, 100) for x in range(5, randint(5, 30))]
# Print the results
print(common_numbers(a, b))
