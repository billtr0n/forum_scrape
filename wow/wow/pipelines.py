# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import pymongo

class WowPipeline(object):
    def process_item(self, item, spider):
        return item
        

class JsonWriterPipeline( object ) :

    def open_spider(self, spider):
        self.file = open('items.json', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class MongoPipeline(object):
    collection_name = 'wow-ptr-items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGODB_SERVER'),
            mongo_db = crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise scrapy.DropItem("Missing data!")
        self.db[self.collection_name].update({'url': item['url']}, dict(item), upsert=True)
        return item
