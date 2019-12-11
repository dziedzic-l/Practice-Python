def get_number():
    '''Returns number typed by the user'''
    return int(input('Enter the number: '))


def is_prime_number(number):
    '''Checks if the given number is prime'''
    # Import math module
    import math

    # Case 1 - The given number is equal to 1
    if number is 1:
        print(f'{number} is not prime and not composite')
        return False
    # Case 2 - The given number is equal to 2
    elif number is 2:
        print(f'{number} is prime')
        return True
    # Case 3 - The given number is greater than 2
    # For each number(n) from range 2 to root of the given number + 1
    for n in range(2, round(math.sqrt(number)) + 1):
        # If the given number is divisible by n
        if number % n == 0:
            print(f"{number} is composite number")
            return False
            break
    # If the given number is prime
    print(f"{number} is prime number")
    return True

is_prime_number(get_number())
