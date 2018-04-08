# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BaiduSpider(CrawlSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    rules =(
        Rule(LinkExtractor(allow=('\.png',)),callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        print(response.url)
        print('-'*40)
