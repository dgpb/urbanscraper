# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def remove_nt(value):
    return value.replace('\t', ' ').replace('\n', ' ')

class UrbanscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    status = scrapy.Field()
    published_date = scrapy.Field()
    views = scrapy.Field()
    type_property = scrapy.Field()
    type_transaction = scrapy.Field()
    price_usd = scrapy.Field()
    contact = scrapy.Field()
    contact_type = scrapy.Field()
    url = scrapy.Field()

    pass
