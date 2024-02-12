import re

import requests
from bs4 import BeautifulSoup

from .models import Book


def crawl(url):
    # Make a GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified tag and attributes
        items = soup.find_all({'tr': 'itemscope'}, itemtype='http://schema.org/Book')

        # Iterate over each item found on the webpage
        for item in items:
            # Extract title of the book
            title = item.find('span', itemprop='name').get_text()

            # Extract author of the book
            author = item.find('span', itemprop='author').get_text().replace('\n', '').strip()

            # Extract rating of the book
            rating_text = item.find('span', class_='minirating').get_text()
            rating = re.search(r'\b\d+(?:\.\d+)?\b', rating_text).group()

            # Extract published year of the book
            published_text = item.find('span', class_='minirating').next_sibling.get_text()
            year_item = re.findall(r'\d+', published_text)
            year = year_item[0] if len(year_item) > 0 else 0

            # Create a Book instance with extracted information and save it to the database
            book = Book.objects.create(
                title=title,
                author=author,
                rating=float(rating),
                published_year=int(year)
            )

        # Return the last created Book instance
        return book

    else:
        # If request failed, print an error message
        print('Failed to retrieve the webpage')

    # Return None if no book was created
    return None
