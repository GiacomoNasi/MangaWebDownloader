from image_url_providers.image_url_provider import ImageUrlProvider
from image_url_providers.image_url_provider_hastareader import ImageUrlProviderHastareader
from image_url_providers.image_url_provider_mangaworld import ImageUrlProviderMangaworld


def get_image_url_downloader(manga_url, manga_html) -> ImageUrlProvider:

    if 'mangaworld' in manga_url:
        return ImageUrlProviderMangaworld(manga_html)

    elif 'reader.hastateam' in manga_url:
        return ImageUrlProviderHastareader(manga_html)

    raise Exception(f'Image url downloader not found for {manga_url}')