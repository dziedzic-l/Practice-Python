# import datetime module
import datetime

# Ask for user's name and age
name = input('Enter your name: ')
# Check if name contains only letters
if not name.isalpha():
    raise Exception('The name can only contain letters')
# Get the user's age and convert the value to integer type
# using int() function
age = int(input('Enter your age: '))
# Get the number of repetition number.
repetitions = int(input('How many times to repeat a message: '))

# Get actual year using datetime module
actual_year = datetime.date.today().year
# Calculate the year on user's 100th birthday
year_on_100th_birthday = actual_year + (100 - age)

# Depending on age, display the right message
if age > 100:
    message = f'Your 100th birthday was in {year_on_100th_birthday}'
elif age < 100:
    message = f'Your 100th birthday will be in {year_on_100th_birthday}'
else:
    message = f'Your 100th birthday is in {year_on_100th_birthday}'

# Depending on repetitions number, display the right number of message
for x in range(repetitions):
    print(f'{name.capitalize()}, {message} \n')
