import sys
from src.crawler import Crawler

if __name__== "__main__":
    crawler = Crawler([url for url in sys.stdin])
    crawler.crawl()
