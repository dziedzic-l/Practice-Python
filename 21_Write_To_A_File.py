import requests
from bs4 import BeautifulSoup

# Make a GET request to given address
response = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, features="html.parser")
# Get all paragraphs inside div with article__body class
article = soup.select('div.article__body > p')

# A variable that will store filename
filename = ''

while filename == '':
    filename = input('Enter the filename: ')

# Open the file in read mode
with open(filename, 'w') as file:
    for paragraph in article:
        file.write(paragraph.getText())
