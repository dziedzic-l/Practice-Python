categories_count = {}

with open('this.txt', 'r') as tfile:
    for line in tfile.readlines():
        # Get category name
        category = line.split('/')[2]
        # If category exists in dictionary
        if category in categories_count:
            categories_count[category] += 1
        else:
            categories_count[category] = 1

print(categories_count)
