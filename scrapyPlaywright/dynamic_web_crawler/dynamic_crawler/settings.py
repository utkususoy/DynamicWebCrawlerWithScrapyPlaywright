# -*- coding: utf-8 -*-

# Bot name
BOT_NAME = 'web_spider'

# Modules where spiders are located
SPIDER_MODULES = ['dynamic_crawler.spiders']
NEWSPIDER_MODULE = 'dynamic_crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Playwright settings for launching the browser
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True}
PLAYWRIGHT_BROWSER_TYPE = 'chromium'

# Download handlers for Playwright integration
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Twisted reactor setting for async support
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Additional browser options for Playwright
# PLAYWRIGHT_BROWSER_OPTIONS = {
#     "network_idle_timeout": 100000  # Adjust the timeout as needed
#     # "viewport": {"width": 1920, "height": 1080}
# }
