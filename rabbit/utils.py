# -*- coding: utf-8 -*-


# third-party
import requests
from bs4 import BeautifulSoup


def title_scraper(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, features='html.parser')
    site_title = soup.find('meta', attrs={'property': 'og:title'})
    title = None
    if site_title:
        title = site_title.get('content')
    elif soup.title.text:
        title = soup.title.text
    return title


def image_scraper(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, features='html.parser')
    site_image = soup.find('meta', attrs={'property': 'og:image'})
    image = None
    if site_image:
        image = site_image.get('content')
    else:
        site_image = soup.find('meta', attrs={'property': 'og:icon'})
        if site_image:
            image = site_image.get('content')
    return image
