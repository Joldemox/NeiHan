# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter


class NeihanbaPipeline(object):
    def process_item(self, item, spider):
        # 默认现在没有开启管道，所以现在不会进入文件写入
        self.writer.export_item(item)
        return item

    def open_spider(self, spider):
        self.file = open('neihanba.json', 'wb')  # 源码中是以二进制的列表进行写入的
        # 写入器
        self.writer = JsonItemExporter()
        self.writer.start_exporting()

    def close_spider(self, spider):
        # 需要先关闭写入器再关闭文件
        self.writer.finish_exporting()
        self.file.close()
