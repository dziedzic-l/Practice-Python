# Get the numbers to check
num = int(input('Enter the number to check: '))
check = input('Enter the second number: ')

# If check variable is not empty and contains only digits
if check and check.isdigit():
    # Convert value of check variable to integer type
    check = int(check)
    # If value of check variable divides evenly into num 
    if num % check == 0:
        print('Check divides evenly into num')
    else:
        print('Check not divides evenly into num')
else:
    # If the number is divisible by 4
    if num % 4 == 0:
        print('This number is divisible by 4')
    # If the number is divisible by 2
    elif num % 2 == 0:
        print('This number is even')
    # If the number is not divisible by 2
    else:
        print('This number is odd')
