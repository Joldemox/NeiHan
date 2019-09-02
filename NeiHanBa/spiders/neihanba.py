# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 继承了Spider的子类CrawlSpider
class NeihanbaSpider(CrawlSpider):
    name = 'neihanba'
    allowed_domains = ['neihanba.com']
    start_urls = ['https://www.neihanba.com/dz/index.html']

    # 提取规则
    # 根据设定的规则，自动提取链接
    # 自动发送请求，解析response
    rules = (
        # Rule(LinkExtractor(allow=r'list'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'list')),
    )

    # 解析函数，没有指定名称，因为parse已经在模块中被指定了
    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

        print('*' * 100)
        print(response.url)
