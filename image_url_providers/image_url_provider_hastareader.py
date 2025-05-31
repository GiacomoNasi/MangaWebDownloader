from pathlib import PurePosixPath
from urllib.parse import urlparse

from image_url_providers import utils
from image_url_providers.image_url_provider import ImageUrlProvider


class ImageUrlProviderHastareader(ImageUrlProvider):
    # It could be impossible to implement: looks like it is hard to deduce png urls since thay are not present in manga hml
    # and they are very different from manga url


    def __init__(self, manga_html):
        self.first_image = utils.get_png_urls(manga_html)[0]

    # https://reader.hastateam.com/storage/comics/berserk_5044a192012db/it-5-2-N-002_0_zodd_limmortale_1_508bebaa6641b/Berserk%20-%20vol%2005%20144.png?v=1351339930
    def get_png_url(self, index: int) -> str | None:
        pass


