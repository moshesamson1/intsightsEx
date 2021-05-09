import requests
from lxml import html

SUCCESS = 200


class Downloader:
    def downloadPage(url: str):
        print("downloading url: ", url)
        page = requests.get(url)
        if page.status_code == SUCCESS:
            return html.fromstring(page.content)
        else:
            print("ERROR: could not load page! err message is: ", page.reason)
        return None
