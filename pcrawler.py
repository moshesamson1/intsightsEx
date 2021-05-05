from downloader import Downloader
from twisted.internet import task, reactor
timeout = 600.0 # 10 min timeout

PASTES_ARCHIVE_URL = "https://pastebin.com/archive"

def doWork():
    print("doing some work")
    tree = Downloader.downloadPage(PASTES_ARCHIVE_URL)
    

def main():
    l = task.LoopingCall(doWork)
    l.start(timeout)
    reactor.run()


if __name__ == "__main__":
    print("initiate web crawler")
    main()