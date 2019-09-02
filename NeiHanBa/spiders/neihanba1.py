# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 继承了Spider的子类CrawlSpider
from NeiHanBa.items import NeihanbaItem


class NeihanbaSpider(CrawlSpider):
    name = 'neihanba1'
    allowed_domains = ['neihanba.com']
    start_urls = ['https://www.neihanba.com/dz/index.html']

    # 提取规则
    # 根据设定的规则，自动提取链接
    # 自动发送请求，解析response
    rules = (
        Rule(LinkExtractor(allow=r'list'), ),
        Rule(LinkExtractor(allow=r'\d+'), callback='parse_detail', ),
        # Rule(LinkExtractor(allow=r'list')),
    )

    # 解析函数，没有指定名称，因为parse已经在模块中被指定了
    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

        # print('*' * 100)
        # print(response.url)
        pass

    def parse_detail(self, response):
        # pass
        item = NeihanbaItem()
        item['title'] = response.xpath('/html/body/div[1]/div[2]/div[2]/h1/text()').extract_first()
        item['time'] = response.xpath('/html/body/div[1]/div[2]/div[2]/p/text()').extract_first()
        # 因为实际的html中没有tbody标签，这个标签是网页在前端自己渲染上去的，所以可以直接去掉，或者用//进行跳过
        item['content'] = response.xpath('//div[@id="adcon"]/table//tr/td/p/text()').extract_first().strip()
        # p标签下的内容为空，无法取到
        # yield item
        print(item)