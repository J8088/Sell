# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawler.models import ScrapyItem
import urllib.request
import json


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),  # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items, ensure_ascii=False)
        item.save()

    def process_item(self, item, spider):
        self.items.append(item)
        # urllib("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
        urllib.request.urlretrieve(item['image_url'], item['full_file_name'])
        return item
