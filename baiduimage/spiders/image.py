# -*- coding: utf-8 -*-
import json

import scrapy

from baiduimage.items import BaiduimageItem
from baiduimage.pipelines import BaiduimagePipeline


class ImageSpider(scrapy.Spider):
    keyWord=input("请输入要爬取的图片关键词：")
    name = 'image'
    # allowed_domains = ['baidu.com']
    start_urls = ['https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+keyWord+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word='+keyWord+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30']
    print(start_urls)
    def parse(self, response):
        images=json.loads(response.body)["data"]
        for img in images:
            item = BaiduimageItem()
            try:
                item["imageUrl"] = img["thumbURL"]
                yield item
            except Exception as e:
                print("出错啦")

