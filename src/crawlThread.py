import threading
import urllib.request
import json
import re

class CrawlThread(threading.Thread):

    def __init__(self, seed):
        self.seed = seed

    def parse_html(self):
        try:
            with urllib.request.urlopen(self.seed) as response:
                data = response.read().decode('utf-8')
            print(json.dumps({"website": self.seed, "logo": self.analyze_html_for_logo(data), \
                   "phone": self.analyze_html_for_phones(data)}))
        except:
            pass

    def run(self):
        self.parse_html()

    def analyze_html_for_phones(self, webpageHtml):
        res = re.findall(r"\d+ \d+ \d+", webpageHtml)
        return res

    def analyze_html_for_logo(self, webpageHtml):
        res = re.findall(r"http\S+jpg", webpageHtml.lower())
        return res
