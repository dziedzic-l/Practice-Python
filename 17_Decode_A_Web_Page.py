import requests
from bs4 import BeautifulSoup


def get_article_titles():
    # Make a GET request to given address
    response = requests.get('https://www.nytimes.com/')
    # Get content from the response
    content = response.content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(content, features="html.parser")
    # Find all <article> tags
    articles = soup.find_all('article')
    # List that will store all titles
    titles = []

    # For each article in articles
    for article in articles:
        # Find <h2> tag inside <article>
        if article.find('h2'):
            # Add title to titles list
            titles.append(article.find('h2').getText())
    return titles


# Print the results
print(get_article_titles())
