from scrapy.crawler import CrawlerProcess
from dynamic_web_crawler.dynamic_crawler.spiders.web_spider import WebSpiderSpider
from scrapy import signals
from scrapy.signalmanager import dispatcher

class ScrapyCrawler:
    def __init__(self, custom_settings):
        self.custom_settings = custom_settings
        self.content_metadata = {}

    def construct_scrapy_metadata(self, scrapy_item):
        self.content_metadata['image_urls'] = scrapy_item['image_urls']

    def item_collected(self, item, response, spider):
        # This function is called whenever an item is collected
        print("Item collected:", item)
        self.construct_scrapy_metadata(scrapy_item=item)

    def run_crawler(self):
        process = CrawlerProcess(settings=self.custom_settings)
        dispatcher.connect(self.item_collected, signal=signals.item_scraped)
        process.crawl(WebSpiderSpider)
        process.start()  # Blocking call, will finish when crawling is done

        return self.content_metadata