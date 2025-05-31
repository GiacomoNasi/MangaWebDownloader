from typing import Union

import requests
from bs4 import BeautifulSoup

from image_url_providers import utils
from image_url_providers.image_url_provider import ImageUrlProvider


class ImageUrlProviderMangaworld(ImageUrlProvider):

    def __init__(self, manga_html):
        self.image_urls = utils.get_png_urls(manga_html)


    def get_png_url(self, index: int) -> str | None:
        try:
            return self.image_urls[index]
        except IndexError:
            return None

