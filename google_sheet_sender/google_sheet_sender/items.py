# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from enum import Enum

import scrapy
from itemloaders.processors import TakeFirst


class BookItem(scrapy.Item):
    ...
