# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from sunnder.items import SunnderItem

class ItemParser(object):
    album = "qdailyy"

    def parseAlbum(self, response):
        articles = response.xpath('//a[@class="com-grid-article"]/@href').extract()
        albumx = response.xpath('//div[@class="column-detail-header-hd"]//span[@class="title"]/text()').extract_first()
        self.album = albumx
        for aurl in articles:
            yield scrapy.Request("http://www.qdaily.com" + aurl, self.parseArticle)

    def parseArticle(self, response):
        item = SunnderItem()

        item['source_url'] = response.url
        item['album'] = self.album
        item['tags'] = response.xpath("//div[@class='article-detail-ft']//a/text()").extract()
        item['image_urls'] = response.xpath("//div[@class='article-detail-hd']/img/@data-src").extract()
        item['title'] = response.xpath('//h2[@class="title"]/text()').extract_first()
        cate = response.xpath('//div[@class="category-title"]//span/text()')
        #if len(cate)>=2:
        item['category'] = cate.extract()[0]
        item['author'] = response.xpath('//div[@class="author"]//span[@class="name"]/text()').extract_first()
        ocontent = response.xpath('//div[@class="detail"]').extract()
        cc = ""
        if(len(ocontent)!=0):
            for c in ocontent:
                cc = cc+c
        item['content'] = cc

    	# self.logger.info('xxxitem: %s,', response.xpath("//div[@class='conText']//img/@src").extract())
    	#self.logger.info('item: %s,', item)
        return item

class QdailySpider(scrapy.Spider):
    name = "qdaily"
    allowed_domains = ["qdaily.com"]
    start_urls = [
        "http://www.qdaily.com/special_columns.html",
	]

    def parse(self, response):
        albums = response.xpath('//a[@class="com-grid-column"]/@href').extract()
        for aurl in albums:
            self.logger.info("%s", "http://www.qdaily.com" + aurl)
            itemParser = ItemParser()
            yield scrapy.Request("http://www.qdaily.com" + aurl, itemParser.parseAlbum)
            
    













