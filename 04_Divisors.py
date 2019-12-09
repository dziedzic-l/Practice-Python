# Get the number from user input
number = int(input('Enter the nuber: '))
# Empty lists that will store divisors
divisors1 = []
divisors2 = []

# Method 1
# For each number in range 1 to number given by the user
for n in range(1, number):
    # If number is divisible by n
    if number % n is 0:
        # Add divisor to divisors1 list
        divisors1.append(n)

# Method 2 using list comprehension
divisors2 = [m for m in range(1, number) if number % m is 0]

# Print the results
print(divisors1)
print(divisors2)
