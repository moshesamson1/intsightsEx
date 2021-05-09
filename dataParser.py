from paste import Paste
from downloader import Downloader
import arrow
import dateutil

class DataParser:
    def parse_link(url:str) -> Paste:
        tree = Downloader.downloadPage(url)
        if tree is None: return None
        
        try :
            date = tree.xpath('//div[@class="date"]//span/@title')[0]
            username = tree.xpath('//div[@class="username"]//a/text()')[0]
            title = tree.xpath('//div[@class="details"]//div[@class="info-bar"]//div[@class="info-top"]//h1/text()')[0]
            content = tree.xpath('//textarea/text()')[0]
        except : 
            print("Failed to process url: ", url)
            return None
        
        # todo: validate fetched results
        return Paste(author=username, title=title, content=content, datetime=DataParser.strdate_to_arrow(date), link=url.split('/')[-1])
    
    def strdate_to_arrow(strdate: str) -> arrow.Arrow:
        basic_date = arrow.get(strdate, 'dddd Do [of] MMMM YYYY hh:mm:ss A')
        basic_date_fix_tz = fix_time_zone(basic_date, strdate.split(' ')[-1])
        normalized_date = basic_date_fix_tz.to('utc')
        return normalized_date

def fix_time_zone(basicdate:arrow.Arrow, tz_string:str=""):
    # as far as I can see, all times comes with CDT abbrevian for timezone, which can be several timezones
    # I chose the us central, and used it throughout the process, failing in case a new one is submitted 
    if tz_string != "CDT":
        print("ERR: got unknown timezone: ", tz_string)
        exit(2)
    return basicdate.replace(tzinfo=dateutil.tz.gettz('US/Central'))