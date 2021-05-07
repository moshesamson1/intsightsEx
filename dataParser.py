from paste import Paste
from downloader import Downloader

class DataParser:
    def parse_link(url:str) -> Paste:
        tree = Downloader.downloadPage(url)
        if tree is None: return None
        date = tree.xpath('//div[@class="date"]//span//@title')
        print(date)
        return Paste("me", "titlestring", "content", "123")
    # extract the main table object