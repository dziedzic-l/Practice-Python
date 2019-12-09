# Sample list of numbers
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Get the number entered by the user
limit = int(input("Enter the number: "))
# Empty list that will contains numbers 
# that are smaller than that number given by the user 
less_than_five1 = []

# Method 1
# For each number in a list
for number in a:
    # If number is less than number given by the user
    if number < limit:
        # Add the number to less_than_five1 list
        less_than_five1.append(number)

# Method 2
less_than_five2 = [number for number in a if number < limit]

print(less_than_five1)
print(less_than_five2)
