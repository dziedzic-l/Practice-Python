def find_element(number, list_to_search):
    '''Searches for an item in the given list using binary search'''
    list_to_search.sort()

    # Starting position of the first element of a given list
    left = 0
    # Starting position of last element of a given list
    right = len(list_to_search) - 1

    while left < right:
        # Calculate position of middle element of a given list
        middle = (left + right) // 2

        # Check if the number you are looking for is greater
        # than the number in the list at the given position
        if number > list_to_search[middle]:
            left = middle + 1
        else:
            right = middle

    # Check if the number is on the list
    if number == list_to_search[left]:
        print(f'Found in position {left}')
    else:
        print("Not found")


numbers = [1, 3, 4, 2, 5, 6, 9, 8]

find_element(4, numbers)
