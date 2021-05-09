from paste import Paste
from downloader import Downloader
import arrow

class DataParser:
    def parse_link(url:str) -> Paste:
        tree = Downloader.downloadPage(url)
        if tree is None: return None
        
        try :
            date = tree.xpath('//div[@class="date"]//span/text()')[0]
            username = tree.xpath('//div[@class="username"]//a/text()')[0]
            title = tree.xpath('//div[@class="details"]//div[@class="info-bar"]//div[@class="info-top"]//h1/text()')[0]
            content = tree.xpath('//textarea/text()')[0]
        except : 
            print("Failed to process url: ", url)
            return None
        
        # todo: validate fetched results
        return Paste(author=username, title=title, content=content, datetime=DataParser.strdate_to_arrow(date), link=url.split('/')[-1])
    
    def strdate_to_arrow(strdate: str) -> arrow.Arrow:
        return arrow.get(strdate, 'MMMM D[(st|nd|rd|th)], YYYY')