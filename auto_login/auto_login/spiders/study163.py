# -*- coding: utf-8 -*-
import scrapy

from auto_login.items import AutoLoginItem


class Study163Spider(scrapy.Spider):
    name = 'study163'
    allowed_domains = ["csdn.net"]
    # start_urls = ['https://study.163.com/passport/cellphone/login.htm']

    def start_requests(self):
        print("开始登录。。。")
        # return [scrapy.Request('https://study.163.com/passport/cellphone/login.htm',headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        #                                                                                      "Content - Type": "application / x - www - form - urlencoded",
        #                                                                                      "Cookie": '__q_=1;_ntes_nnid = 6e3016402b7d67e2b1ee6f2a397fa4e6;usertrack = ezq0pVoyT8SBC7KBBqZhAg ==;_ga = GA1.2.1504938150.1513246684;__e_ = 1514855360200;EDUWEBDEVICE = 23985206e2f54a9fabe3fe81953dc727;videoVolume = 0.8;videoResolutionType = 3;__utmc = 129633230;sideBarPost = 560;__utmz = 129633230.1516268606.6.3.utmcsr = baidu | utmccn = (organic) | utmcmd = organic;__utma = 129633230.1504938150.1513246684.1516268606.1516268606.7;NETS_STUDY_REG = 2582f384be0daa2c088d8b5b42bfcdd2544012445f798b1f078e0c9ccaa6448b;st_autoregister = 1;utm = "eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9zdHVkeS4xNjMuY29tL2NvdXJzZXM/ZnJvbT1zdHVkeQ==";STUDY_CP_ENTRANCE_CLOSE = 1;NTESSTUDYSI = 8924ff8fe03349c1b2f2e6b938cde42c;__utmb = 129633230.37.9.1516327304622',
        #                                                                                      "Host": "study.163.com",
        #                                                                                      "Origin": "https: // study.163.com",
        #                                                                                      "Referer": "https: // study.163.com / member / logoutResult.htm"},
        #                        callback=self.post_login, method="POST")]
        # return [scrapy.Request('https://study.163.com/topics/smartspec_nianzhong?utm_source=baidu&utm_medium=cpc&utm_campaign=affiliate&utm_term=nianzhong_Brand03&utm_content=SEM',callback=self.post_login)]
        return [scrapy.Request("https://passport.csdn.net/account/login",callback=self.__post_login)]

    @staticmethod
    def __get_key_value(response, keystr):
        # '用来得到关键字段的值'
        # '或者通过css选取器可以如下'
        # return response.css('input[name="lt"] ::attr(value)').extract_first()
        # '或者通过xpath可以如下'
        return response.xpath(u'//input[@name=\"{0}\"]/@value'.format(keystr)).extract_first()

    def __post_login(self, response):
        # '通过post登陆'
        post_data = {
            'username': "18380461696",
            'password': "yj876993",
            'lt': Study163Spider.__get_key_value(response, 'lt'),
            # 'gps': Study163Spider.__get_key_value(response, 'gps'),
            'execution': Study163Spider.__get_key_value(response, 'execution'),
            '_eventId': 'submit',
        }
        print(post_data["lt"])
        print(post_data["execution"])
        return [scrapy.FormRequest.from_response(response, formdata=post_data, callback=self.after_login)]

    def after_login(self,response):
        return scrapy.Request("http://msg.csdn.net/",callback=self.check)

    def check(self,reponse):
        fail=reponse.xpath("//div[@class='login-part']/h3/text()")
        success=reponse.xpath("//a[@class='mark_read']/text()")
        if len(fail)>0:
            print("登录失败")
        if len(success)>0:
            print(success.extract())
            print("登录成功")
        link_list=reponse.xpath("//ul[@class='long_title_list']")
        for link in link_list:
            item=AutoLoginItem()
            item["link"]=link.xpath("./li/text()").extract_first()
            yield item