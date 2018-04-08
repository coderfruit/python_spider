# -*- coding: utf-8 -*-
import scrapy

from firstspider.items import FirstspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://sou.zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=2040&in=160400&jl=%E6%88%90%E9%83%BD&p=1&isadv=0']
    def parse(self, response):
        node_list = response.xpath("//table[@class='newlist']/tr[1]")
        print(len(node_list))
        for node in node_list:
            if len(node.xpath("./td[5]/text()").extract())==0:
                print("没找到数据。。。")
                pass
            else:
                item = FirstspiderItem()
                item["positionName"]=node.xpath("./td[1]/div/a/text()").extract()[0]

                item["rate"]=node.xpath("./td[2]/span/text()").extract()
                if len(item["rate"])==0:
                    item["rate"]="0%"
                else:
                    item["rate"]=node.xpath("./td[2]/span/text()").extract()[0]

                item["companyName"]=node.xpath("./td[3]/a[1]/text()").extract()[0]

                item["salary"]=node.xpath("./td[4]/text()").extract()[0]

                item["workLocation"] = node.xpath("./td[5]/text()").extract()[0]

                item["publishTime"] = node.xpath("./td[6]/span/text()").extract()[0]
                yield item
        # 一页数据爬完后，获取下一页的链接，然后再构造请求，交给下载器下载，最后通过回调函数parse抓取数据
        nextUrl=response.xpath("//div[@class='pagesDown']/ul/li[@class='pagesDown-pos']/a/@href")
        if len(nextUrl)==0:
            print("最后一页啦。。。。")
            return
        else:
            print("爬取下一页")
            yield scrapy.Request(nextUrl.extract()[0], callback=self.parse,dont_filter=True)



