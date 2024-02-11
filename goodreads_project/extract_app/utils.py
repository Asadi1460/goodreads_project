import re

import requests
from bs4 import BeautifulSoup

from .models import Book


def crawl(URL):
    response = requests.get(URL)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.find_all({'tr': 'itemscope'}, itemtype='http://schema.org/Book')
        # print('items', items[0])

        for item in items:
            # Extract title
            title = item.find('span', itemprop='name').get_text()

            # Extract author
            author = item.find('span', itemprop='author').get_text().replace('\n', '').strip()

            # Extract Rating
            rating_text = item.find('span', class_='minirating').get_text()
            rating = re.search(r'\b\d+(?:\.\d+)?\b', rating_text).group()

            # Extract publisher
            published_text = item.find('span', class_='minirating').next_sibling.get_text()
            year_item = re.findall(r'\d+', published_text)
            year = year_item[0] if len(year_item) > 0 else 0

            # edition_text = item.find('span', class_='minirating').next_sibling.get_text()
            # edition_item = re.findall(r'\d+ editions', edition_text)
            # edition = edition_item
            # print("Edition:", edition)


            # Create a Book instance and save it to the database
            book = Book.objects.create(
                title=title,
                author=author,
                rating=float(rating),
                published_year=int(year)
            )

        return book  # Return the created Book instance

    else:
        print('Failed to retrieve the webpage')
    return None
