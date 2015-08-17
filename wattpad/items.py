# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WattpadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    part = scrapy.Field()
    fictiontype = scrapy.Field()
    read = scrapy.Field()
    like = scrapy.Field()
    content = scrapy.Field()

    