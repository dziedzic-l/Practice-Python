# Get number of numbers to display
how_many = int(input('How many numbers to display: '))


def fibonacci(x):
    '''Returns list of fibonacci numbers'''
    if x == 0:
        return []
    if x == 1:
        return [1]
    else:
        fibonacci = [0, 1]
        for n in range(2, x + 1):
            fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])

    return fibonacci

print(fibonacci(how_many))
