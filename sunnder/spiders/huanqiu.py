# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from sunnder.items import SunnderItem

class HuanqiuSpider(scrapy.Spider):
    name = "huanqiu"
    allowed_domains = ["huanqiu.com"]
    start_urls = [
	"http://www.huanqiu.com/",
	# "http://world.huanqiu.com/article/2017-04/10420439.html",
	]

    def parse(self, response):
    	articles = response.xpath('//a/@href').extract()
    	for aurl in articles:
    		yield scrapy.Request(aurl, self.parseArticle)

    def parseArticle(self, response):
    	item = SunnderItem()

    	item['image_urls'] = response.xpath("//div[@class='conText']//img/@src").extract()
    	item['title'] = response.xpath('//div[@class="conText"]//h1/text()').extract_first()
    	cate = response.xpath('//div[@class="topPath"]//a/text()')
    	if len(cate)>=2:
    		item['category'] = cate[1].extract()
    	item['author'] = response.xpath('//div[@class="summaryNew"]//strong[@class="fromSummary"]//a/text()').extract_first()
    	ocontent = response.xpath('//div[@class="conText"]//p').extract()
    	cc = ""
    	if(len(ocontent)!=0):
    		for c in ocontent:
    			cc = cc+c
    	item['content'] = cc

    	# self.logger.info('xxxitem: %s,', response.xpath("//div[@class='conText']//img/@src").extract())
    	self.logger.info('item: %s,', item)
    	return item















