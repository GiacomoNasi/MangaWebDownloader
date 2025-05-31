import requests_cache


def get_image(image_url):
    session = requests_cache.CachedSession('png_caches')
    return session.get(image_url).content
