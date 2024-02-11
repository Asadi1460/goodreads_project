import re

import requests
from bs4 import BeautifulSoup


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
            print("Title:", title)

            # Extract author
            author = item.find('span', itemprop='author').get_text().replace('\n', '').strip()
            print("Author:", author)

            # Extract Rating
            rating_text = item.find('span', class_='minirating').get_text()
            rating = re.search(r'\b\d+(?:\.\d+)?\b', rating_text).group()
            # rating = re.findall(r'\d+(?:\.\d+)?', rating_text)
            print("Rating", rating)

            # Extract publisher
            published_text = item.find('span', class_='minirating').next_sibling.get_text()
            year_item = re.findall(r'\d+', published_text)
            year = year_item[0] if len(year_item) > 0 else None
            print("Published Year:", year)

            # edition_text = item.find('span', class_='minirating').next_sibling.get_text()
            # edition_item = re.findall(r'\d+ editions', edition_text)
            # edition = edition_item
            # print("Edition:", edition)

            print('=' * 50)


    else:
        print('Failed to retrieve the webpage')
    return None


URL = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q=python&search_type=books'

crawl(URL)
