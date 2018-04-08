# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json


class FirstspiderPipeline(object):
    def __init__(self):
        self.f=open("data.csv",mode="w",newline="")
        self.wr = csv.writer(self.f)
        self.wr.writerow(["职位名称","反馈率","公司名称","薪资","工作地点","发布时间"])

    def process_item(self, item, spider):
        # data=json.dumps(dict(item),ensure_ascii=False)+",\n"
        # data=dict(item)
        # print(data)
        data=[item["positionName"],item["rate"],item["companyName"],item["salary"],item["workLocation"],item["publishTime"]]
        self.wr.writerow(data)
        return item

    def close_spider(self,spider):
        self.f.close()
