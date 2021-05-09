from paste import Paste
from downloader import Downloader

class DataParser:
    def parse_link(url:str) -> Paste:
        tree = Downloader.downloadPage(url)
        if tree is None: return None
        
        try :
            date = tree.xpath('//div[@class="date"]//span//@title')[0]
            username = tree.xpath('//div[@class="username"]//a/text()')[0]
            title = tree.xpath('//div[@class="details"]//div[@class="info-bar"]//div[@class="info-top"]//h1/text()')[0]
            content = tree.xpath('//textarea/text()')[0]
        except : 
            print("Failed to process url: ", url)
            return None
        
        # todo: validate fetched results
        return Paste(author=username, title=title, content=content, datetime=date)