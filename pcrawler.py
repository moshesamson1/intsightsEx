from twisted.internet import task, reactor
timeout = 5.0

def doWork():
    print("doing some work")

def main():
    l = task.LoopingCall(doWork)
    l.start(timeout)
    reactor.run()


if __name__ == "__main__":
    print("initiate web crawler")
    main()