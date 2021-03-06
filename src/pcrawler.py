from downloader import Downloader
from dataParser import DataParser
from dataManager import DataManager
from twisted.internet import task, reactor
import multiprocessing.dummy
import time

p = multiprocessing.dummy.Pool(10)
timeout = 120.0  # 2 min timeout

PASTES_ARCHIVE_URL = "https://pastebin.com"

# should be done before fetching, and be initialized
# accprding to db/local storage of data
processed_links = DataManager.get_existing_pastes()


def crawl_pastes():
    print("doing some work")
    tree = Downloader.downloadPage(PASTES_ARCHIVE_URL+"/archive")
    paste_links = tree.xpath('//table[@class="maintable"]//tbody\
        //tr//td[1]//a//@href')

    start = time.time()
    pastes = p.map(
        DataParser.parse_link,
        [PASTES_ARCHIVE_URL+paste_rel_link for paste_rel_link in paste_links
            if paste_rel_link[1:] not in processed_links]
    )
    p.starmap(
        DataManager.saveToFile,
        [(p, p.relative_link) for p in pastes if p is not None]
    )

    processed_links.extend([p.removeprefix('/') for p in paste_links])
    print("took " + str(time.time() - start))


def main():
    looping_call = task.LoopingCall(crawl_pastes)
    looping_call.start(timeout)
    reactor.run()


if __name__ == "__main__":
    print("initiate web crawler")
    main()
