from downloader import Downloader
from dataParser import DataParser 
from twisted.internet import task, reactor
import multiprocessing.dummy
import time

p = multiprocessing.dummy.Pool(10)
timeout = 600.0 # 10 min timeout

PASTES_ARCHIVE_URL = "https://pastebin.com"

def doWork():
    print("doing some work")
    tree = Downloader.downloadPage(PASTES_ARCHIVE_URL+"/archive")
    paste_links = tree.xpath('//table[@class="maintable"]//tbody//tr//td[1]//a//@href')
    
    start = time.time()
    p.map(DataParser.parse_link, [PASTES_ARCHIVE_URL+paste_rel_link for paste_rel_link in paste_links])
    print("took " +str( time.time() - start))
    # DataParser.parse_link("")
    # print(main_table)
    

def main():
    l = task.LoopingCall(doWork)
    l.start(timeout)
    reactor.run()


if __name__ == "__main__":
    print("initiate web crawler")
    main()