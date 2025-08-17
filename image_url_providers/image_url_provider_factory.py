from image_url_providers.image_url_provider import ImageUrlProvider
from image_url_providers.image_url_provider_basic import ImageUrlProviderBasic
from image_url_providers.image_url_provider_hastareader import ImageUrlProviderHastareader


def get_image_url_downloader(manga_url, manga_html) -> ImageUrlProvider:

    # if 'mangaworld' in manga_url:
    #     return ImageUrlProviderBasic(manga_html)

    if 'reader.hastateam' in manga_url:
        return ImageUrlProviderHastareader(manga_html)

    print(f'Image url downloader not found for {manga_url}, defaulting in ImageUrlProviderBasic')
    return ImageUrlProviderBasic(manga_html)

    # raise Exception(f'Image url downloader not found for {manga_url}')