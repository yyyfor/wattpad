from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from wattpad.items import WattpadItem

class WattpadSpider(Spider):
    name = "wattpad"
    allowed_domains = ["https://www.wattpad.com"]
    start_urls = [
        "https://www.wattpad.com/search/music",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="content"]')

        for question in questions:
            item = WattpadItem()
            item['title'] = question.xpath(
                'h5/text()').extract()[0]
            item['name'] = question.xpath(
                'ul[contains(@class, "story-details")]/li/text()').extract()[0]
            item['part'] = question.xpath(
                'ul[contains(@class, "story-details")]/li/text()').extract()[1]
            item['fictiontype'] = question.xpath(
                'ul[contains(@class, "story-details")]/li/text()').extract()[2]
            item['read'] = question.xpath(
                'div[@class="meta"]/small[@class="reads"]/text()').extract()[0]
            item['like'] = question.xpath(
                'div[@class="meta"]/small[@class="votes"]/text()').extract()[0]
            item['content'] = question.xpath(
                'p/text()').extract()[0]

            yield item