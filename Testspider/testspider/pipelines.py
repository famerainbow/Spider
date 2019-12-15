# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import pymysql

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = '127.0.0.1',user = 'root',password = 'root',db = 'test2',port = 3306)
        self.cursor = self.conn.cursor()
        def process_item(self, item, spider):
            insert_sql = '''
                insert into spider(author,work,tags,url_object_id) values (%s,%s,%s,%s)
            '''
            self.cursor.execute(insert_sql,(item['author'],item['work'],item['tags'],item['url_object_id']))
            self.conn.commit()

class TestspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json','w',encoding = 'utf-8')
    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False) + '\n'    #序列化为str
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()



