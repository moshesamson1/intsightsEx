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
        ts = strdate.split(' ')
        year = int(ts[2])
        day = int(ts[1][:-3])
        month = arrow.get(ts[0],'MMMM').month
        #todo: create formatting string to directly create a arrow object from string
        return arrow.get(year, month, day)