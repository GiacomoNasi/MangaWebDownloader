import datetime
import os
import sys
import tempfile
from tkinter import filedialog, simpledialog

import requests
import requests_cache
from PIL import Image
from bs4 import BeautifulSoup

import image_downloader
from image_url_providers import image_url_provider_factory


def create_pdf(png_files, output_path):
    # Make sure they're sorted as needed
    png_files = sorted(png_files)

    # Open images and convert them to RGB (PDF does not support RGBA)
    images = [Image.open(f).convert("RGB") for f in png_files]

    # Save into a single PDF
    pdf_name = simpledialog.askstring("Input", "Pdf name:")
    if not pdf_name.endswith('.pdf'):
        pdf_name = pdf_name + '.pdf'
    if images:
        images[0].save(os.path.join(output_path, pdf_name), save_all=True, append_images=images[1:])
        print(f"PDF saved as {pdf_name}")
    else:
        print("No images to save.")

#https://www.mangaworld.nz/manga/2278/berserk/read/5fb844014106670a1da640b9/3?style=list https://www.mangaworld.nz/manga/2278/berserk/read/5fb844014106670a1da640bb/1?style=list https://www.mangaworld.nz/manga/2278/berserk/read/5fb844014106670a1da640bc/1?style=list

if __name__ == '__main__':
    png_paths = []

    folder_path = filedialog.askdirectory(title="Select a Folder")

    for manga_url in sys.argv[1:]:

        # resp = requests.get(manga_url)
        #
        # manga_html = resp.content
        #
        # soup = BeautifulSoup(manga_html, 'html.parser')
        # png_urls = []
        #
        # for img in soup.find_all('img'):
        #     src = img.get('src', '')
        #     if src.lower().endswith('.png') or '.png?' in src.lower():
        #         png_urls.append(src)

        if manga_url.startswith('http://') or manga_url.startswith('https://'):
            print(f'Processing manga URL: {manga_url}')

            session = requests_cache.CachedSession('manga_html_cache')

            session = requests.get(manga_url)
            manga_html = session.content
        else:
            print(f'Processing local file: {manga_url}')
            with open(manga_url, 'r', encoding='utf-8') as f:
                manga_html = f.read()

        manga_world_downloader = image_url_provider_factory.get_image_url_downloader(manga_url, manga_html)

        png_urls = manga_world_downloader.image_urls



        for i, url in enumerate(png_urls):
            print(f'Getting image {i + 1}/{len(png_urls)}: {url}')
            content = image_downloader.get_image(manga_url, url)
            png_path = os.path.join(os.path.normpath(folder_path), str(datetime.datetime.now().timestamp()))
            with open(png_path, 'wb') as f:
                f.write(content)

            png_paths.append(png_path)

    create_pdf(png_paths, folder_path)
    for to_remove in png_paths:
        os.remove(to_remove)


