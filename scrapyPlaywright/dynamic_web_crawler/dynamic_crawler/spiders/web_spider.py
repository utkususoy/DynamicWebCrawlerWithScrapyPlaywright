import asyncio
from typing import Iterable
import scrapy
from scrapy import Request
from scrapy_playwright.page import PageMethod
from dynamic_web_crawler.dynamic_crawler.items import ContentItem
from dynamic_web_crawler.helper import should_abort_request

class WebSpiderSpider(scrapy.Spider):
    name = "web_spider"
    # start_urls = [
    #     'https://westwardshippingnews.com/a-mega-visit-by-the-seabourn-venture/'
    # ]
    # custom_settings = {
    #     'PLAYWRIGHT_ABORT_REQUEST': should_abort_request,
    # }

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(
            # url="https://westwardshippingnews.com/1-3-million-overhaul-of-millbay-docks/",
            url="https://westwardshippingnews.com/a-mega-visit-by-the-seabourn-venture/",
            # url = "https://stackoverflow.com/questions/53426322/what-is-the-shortcut-key-to-comment-multiple-lines-using-pycharm-ide",
            meta={
                "dont_merge_cookies": True,
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("set_viewport_size", {"width": 1920, "height": 100000}),  # Set a large viewport size
                    PageMethod("evaluate", "document.body.style.zoom='0.05'"),
                    # PageMethod("wait_for_timeout", 10000), #TODO: Make it random timeout
                    PageMethod("wait_for_selector", "body"),
                    # PageMethod("wait_for_load_state", state="networkidle", timeout=10000),
                    # PageMethod("wait_for_timeout", 10000),  # TODO: Make it random timeout
                    # PageMethod('wait_for_selector', 'img'),

                    # PageMethod("set_viewport_size", {"width": 1920, "height": 10000}),

                ],
                "playwright_page_goto_kwargs": {
                    "wait_until": "networkidle",
                }
            }
        )

    async def parse(self, response):
        image_list = []
        content_item = ContentItem()
        page = response.meta["playwright_page"]
        # await page.wait_for_selector('img')
        # await asyncio.sleep(5) # Sayfayı bekletir
        images = await page.query_selector_all('img')
        for image in images:
            src = await image.get_attribute('src')
            if src: image_list.append(src)
        content_item['image_urls'] = image_list
        yield content_item
        await page.close()
