import json
import os


def list_birthdays():
    '''Displays a list of people with their date of birth'''
    with open('birthdays.json', 'r') as f:
        birthdays = json.load(f)
        for birthday in birthdays:
            print(birthday)


def store_birthday(name, date):
    '''Stores newly created person with his date of birth in .json file'''
    with open('birthdays.json', 'r') as f:
        birthdays = json.load(f)
        birthdays[name] = date

    with open('birthdays.json', 'w') as f2:
        f2.write(json.dumps(birthdays, indent=4))


def find_birthday(name):
    '''Finds and returns date of birth of the given person'''
    with open('birthdays.json', 'r') as json_file:
        birthdays = json.load(json_file)

        if name in birthdays:
            print(f"{name}'s birthday is {birthdays[name]}.")
        else:
            print('Not found.')


def display_menu():
    print('''
    Main menu:
        [1] - List all birthdays
        [2] - Store new birthday
        [3] - Find birthday
        [4] - Exit program
    ''')


while True:
    display_menu()
    option = int(input('I choose: '))
    os.system('clear')

    if option == 1:
        list_birthdays()
    elif option == 2:
        name = input('Enter the name of the person: ')
        birthday_date = input('Enter the birthday date of the person: ')
        store_birthday(name, birthday_date)
    elif option == 3:
        list_birthdays()
        person = input("Who's birthday do you want to look up? ")
        find_birthday(person)
    elif option == 4:
        print('See you next time!')
        exit()
    else:
        print('Unknown option')
