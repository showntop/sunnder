# -*- coding: utf-8 -*-
import scrapy


class QdailySpider(scrapy.Spider):
    name = "qdaily"
    allowed_domains = ["http://www.qdaily.com/"]
    start_urls = ['http://www.qdaily.com/tags/1068.html']

    def parse(self, response):
        print("-----%s: %s-----"%("crawer", "qdaily"))
        articles = response.xpath('//a/@href').extract()
       	print("%s"%(articles))
