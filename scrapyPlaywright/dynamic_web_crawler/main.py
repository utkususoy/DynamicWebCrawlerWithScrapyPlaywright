from scrapy.crawler import CrawlerProcess
from dynamic_web_crawler.dynamic_crawler.spiders.web_spider import WebSpiderSpider
from dynamic_web_crawler.helper import should_abort_request, should_abort_nonrelated_request
from scrapy import signals
from scrapy.signalmanager import dispatcher

from dynamic_web_crawler.scrapy_crawler import ScrapyCrawler


def main():
    custom_settings = {
        'BOT_NAME': 'web_spider',
        'SPIDER_MODULES': ['dynamic_web_crawler.dynamic_crawler.spiders'],
        'NEWSPIDER_MODULE': 'dynamic_web_crawler.dynamic_crawler.spiders',
        'ROBOTSTXT_OBEY': False,
        'PLAYWRIGHT_LAUNCH_OPTIONS': {
            "headless": False,
            "args": ["--start-maximized"]  # Maximize the window
        },
        'PLAYWRIGHT_BROWSER_TYPE': 'chromium',
        'DOWNLOAD_HANDLERS': {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        'TWISTED_REACTOR': "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        'COOKIES_ENABLED': False,
        'COOKIES_DEBUG': True
        # 'PLAYWRIGHT_ABORT_REQUEST': should_abort_nonrelated_request
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'dynamic_web_crawler.dynamic_crawler.middlewares.IgnoreJsTtfMiddleware': 100,
        # }
        # 'SPIDER_MIDDLEWARES': {
        #     "dynamic_web_crawler.dynamic_crawler.middlewares.DynamicCrawlerSpiderMiddleware": 543,
        #     "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": None,
        # }
        # 'PLAYWRIGHT_BROWSER_OPTIONS': {
        #     "network_idle_timeout": 100000  # Adjust the timeout as needed
        #     # "viewport": {"width": 1920, "height": 1080}
        # },
        # 'PLAYWRIGHT_ABORT_REQUEST': should_abort_request
    }

    # process = CrawlerProcess(settings=custom_settings)
    # dispatcher.connect(item_collected, signal=signals.item_scraped)
    # process.crawl(WebSpiderSpider)
    # process.start()
    #RETURN SCRAPED ITEM HERE HERE##
    crawler = ScrapyCrawler(custom_settings=custom_settings)
    items = crawler.run_crawler()
    print("HEEEEEREEEE")
    print(items)

if __name__ == '__main__':
    main()




