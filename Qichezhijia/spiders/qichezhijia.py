# -*- coding: utf-8 -*-
import copy

import scrapy
from scrapy_splash import SplashRequest


class QichezhijiaSpider(scrapy.Spider):
    name = 'qichezhijia'
    allowed_domains = ['k.autohome.com.cn']
    start_urls = ['https://k.autohome.com.cn/a001/']

    def start_requests(self):

        yield scrapy.Request(self.start_urls[0], callback=self.parse, meta={"cookiejar": 1})

    def parse(self, response):
        """
        按车型进行区分
        :param response:
        :return: 进入选定的车型
        """
        print("按照车型进行区分")
        choose_list = response.xpath("//div[@class='findcont']/div[@class='findcont-choose']/a")
        for choose in choose_list:
            item = {}
            item['href'] = "https://k.autohome.com.cn" + choose.xpath("./@href").extract_first()
            item['title'] = choose.xpath('./text()').extract_first()
            return scrapy.Request(item['href'], callback=self.parse_categlory,
                                  meta={"item": item, "cookiejar": response.meta["cookiejar"]})

    def parse_categlory(self, response):
        """
        按照汽车型号进行区分
        :param response:
        :return:
        """
        print("按照汽车型号进行区分")
        item = copy.deepcopy(response.meta.get("item"))
        car_model_list = response.xpath("//ul[@class='list-cont']/li")
        Cookie = "fvlid=1556498692909INDnQoK3C0; sessionid=53754248-0D23-42DD-A705-0D21534DAC5E%7C%7C2019-04-29+08%3A44%3A46.172%7C%7Cwww.baidu.com; autoid=ce24565735b101a70e6b5fc345c0bb8a; area=440104; ahpau=1; sessionuid=53754248-0D23-42DD-A705-0D21534DAC5E%7C%7C2019-04-29+08%3A44%3A46.172%7C%7Cwww.baidu.com; ASP.NET_SessionId=piopkyfyny33wttsgduf2mc1; guidance=true; sessionip=121.33.144.124; autoac=3C45D01BE78E8BEEE0E3AA2FD00569D6; autotc=4A5EF9F23F2E76C30C10FB3F6BDDE7DA; sessionvid=3198BE2C-A413-4507-84DD-622F0C52C373; ahpvno=35; clubUserShow=5012658|692|2|%E6%B8%B8%E5%AE%A2|0|0|0||2019-04-29+21%3A07%3A02|0; clubUserShowVersion=0.1; _fmdata=4Hm5EKSxMXE5X1BsTRHfhRQG6zq1YIvVi4t24PzThZaEYQVB%2FSQRkzeVUY4X5B7zT%2FXR61vGKbCouKY7HEhpq5E%2BWpHrCToGBt4CYtQc9Ns%3D; __ah_uuid_ng=u_5012658; ref=www.baidu.com%7C0%7C0%7C0%7C2019-04-29+21%3A07%3A05.799%7C2019-04-29+08%3A44%3A46.172; ahrlid=1556543198267dFaunn1z3j-1556543235751"
        cookies = dict([i.split("=", 1) for i in Cookie.split(";")])
        for car_model in car_model_list:
            item['car_model_href'] = "https://k.autohome.com.cn" + car_model.xpath(
                "./div[@class='cont-name']/a/@href").extract_first()
            item['name'] = car_model.xpath("./div[@class='cont-name']/a/text()").extract_first()
            item['score'] = "".join(car_model.xpath("./div[3]/a//text()").extract())
            item['cont_text'] = "".join(car_model.xpath("./div[4]/a//text()").extract())
            # return scrapy.Request(item['car_model_href'],callback=self.parse_car_model,meta={'item':item},cookies=cookies)
            return SplashRequest(item['car_model_href'], callback=self.parse_car_model, meta={"item": item},
                                 args={"wait": 1})

    def parse_car_model(self, response):
        print("获取车的具体信息")
        item = copy.deepcopy(response.meta.get('item'))
        # with open('qichezhijia.html','w',encoding='utf-8')as f:
        #     f.write(response.body.decode("utf-8","ignore"))
        message_list = response.xpath("//div[@class='choose-con mt-10']")
        print(len(message_list))
        for message in message_list:
            item['price'] = ''.join([i.strip() for i in message.xpath("./dl[5]//text()").extract()])  # 价格
            item['space'] = ''.join(message.xpath("./div[1]//span[2]//text()").extract())  # 空间
            item['power'] = ''.join(message.xpath("./div[2]//span[2]//text()").extract())  # 动力
            item['control'] = ''.join(message.xpath("./div[3]//span[2]//text()").extract())  # 控制
            item['consume_oil'] = ''.join(message.xpath("./div[4]//span[2]//text()").extract())  # 耗油
            item['comfortable'] = ''.join(message.xpath("./div[5]//span[2]//text()").extract())  # 舒适度
            item['appearance'] = ''.join(message.xpath("./div[6]//span[2]//text()").extract())  # 外观
            item['trim'] = ''.join(message.xpath("./div[7]//span[2]//text()").extract())  # 装饰
            item['worth_cost'] = ''.join(message.xpath("./div[8]//span[2]//text()").extract())  # 性价比
            item['comment_href'] = "https:" + message.xpath(
                "//div[@class='allcont border-b-solid']/a/@href").extract_first()
            print(item)
            return SplashRequest(item['comment_href'], callback=self.parse_comment, meta={"item": item})

    def parse_comment(self, response):
        """获取评论详情"""
        print('获取评论详情')
        item = response.meta.get("item")
        print("parse_comment", response.cookies)
        pass
