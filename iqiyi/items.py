# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field

# -*- coding: utf-8 -*-
class MgtvItem(Item):
    url=Field()
    title=Field()
    eName=Field()
    otherName=Field()
    adaptor=Field()
    director=Field()
    leader=Field()
    kind=Field()
    language=Field()
    duration=Field()
    story=Field()
    keyWord=Field()
    productPerson=Field()
    dubbing=Field()
    executiver=Field()
    original=Field()
    productColtd=Field()
    productionTime=Field()
    licence=Field()
    registration=Field()
    distributColtd=Field()
    source=Field()
    createTime=Field()
    updateTime=Field()
    updator=Field()
        