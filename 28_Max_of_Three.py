# Method 1
def max_of_three1(a, b, c):
    greatest_number = 0

    for number in locals().values():
        if number > greatest_number:
            greatest_number = number
    return greatest_number

# Method 2
def max_of_three2(a, b, c):
    numbers = [a, b, c]

    greatest_number = 0

    for number in numbers:
        if number > greatest_number:
            greatest_number = number
    return greatest_number

# Method 3
def max_of_three3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


print(max_of_three1(5, 2, 3))
print(max_of_three2(5, 2, 3))
print(max_of_three3(5, 2, 3))
