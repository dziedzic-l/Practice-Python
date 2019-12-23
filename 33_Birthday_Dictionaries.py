birthday_dict = {
    'Drew Brees': '01/15/1979',
    'Michael Thomas': '03/03/1993',
    'Alvin Kamara': '07/25/1994'
}

if __name__ == '__main__':
    print('Welcome to the birthday dictionary. We know the birthdays of:')

    for name in list(birthday_dict.keys()):
        print(name)

    person = input("Who's birthday do you want to look up? ")

    if person in birthday_dict:
        print(f"{person}'s birthday is {birthday_dict[person]}.")
    else:
        print('Not found.')
