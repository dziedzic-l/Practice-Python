with open('prime_numbers.txt') as prime_num_file:
    prime_numbers = [int(number) for number in prime_num_file.readlines()]

with open('happy_numbers.txt') as happy_num_file:
    happy_numbers = [int(number) for number in happy_num_file.readlines()]

# Empty list that will contain common numbers between the lists
common_numbers = []

# For each prime number in a prime numbers list
for prime_number in prime_numbers:
    # If prime number exists in happy_numbers list
    if prime_number in happy_numbers:
        # Add number to common_numbers list
        common_numbers.append(prime_number)

print(common_numbers)
