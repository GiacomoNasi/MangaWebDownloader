from bs4 import BeautifulSoup


def get_png_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    image_urls = []

    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.lower().endswith('.png') or src.lower().endswith('.jpg'):
            image_urls.append(src)

    return image_urls