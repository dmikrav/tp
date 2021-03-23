from src.crawlThread import CrawlThread
import threading

def clean(url):
    return url.replace("\r", "").replace("\n", "")

class Crawler:

    def __init__(self, seeds):
        self.seeds = seeds

    def crawl(self):
        n = len(self.seeds)
        threads = [threading.Thread(target=CrawlThread(clean(self.seeds[z])).run) \
                   for z in range(n)]
        for i in range(n):
            threads[i].start()
        for thread in threads:
            thread.join()

