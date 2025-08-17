import os.path

import requests_cache


def get_image(manga_url:str, image_url:str):

    if image_url.startswith('http://') or image_url.startswith('https://'):
        session = requests_cache.CachedSession('png_caches')
        return session.get(image_url).content

    else:
        with open(os.path.join(os.path.dirname(manga_url), image_url), 'rb') as f:
            return f.read()