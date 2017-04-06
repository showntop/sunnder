# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class SunnderPipeline(object):

	def open_spider(self, spider):
	    self.file = codecs.open('items.json', 'w', "utf-8")

	def close_spider(self, spider):
	    self.file.close()

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False)
		line = line + '\n'
		self.file.write(line)
		return item
