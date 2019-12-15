# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from testspider.items import ArticleItem
from utils.common import get_md5


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://lab.scrapyd.cn/']
    start_urls = ['http://lab.scrapyd.cn//']

    def parse(self, response):
        #获取文章url并交给解析函数爬取字段
        post_urls = response.css('div.quote span a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url = post_urls ,callback = self.parse_detail)

        # 获取下一页的url并交给scrapy下载，下载之后交给parse函数
        next_page = response.css('li.next a::attr(href)').extract_first('')
        if next_page:
            yield Request(url = next_page,callback=self.parse)

    def parse_detail(self,response):
        article_item = ArticleItem()

        author = response.xpath('/html/body/div[1]/div/div/div[1]/article/h1/a/text()').extract_first('')
        work = response.xpath('//*[@id="main"]/article/div/p[1]/text()[1]').extract_first('')
        tags = '标签：'+ response.xpath('//*[@id="main"]/article/p//a/text()').extract()
        tags = ','.join(tags)

        article_item['url_object_id'] = get_md5(response.url)
        article_item['author'] = author
        article_item['work'] = work
        article_item['tags'] = tags
        yield article_item


        #css选择器
        #author = response.css('.post-title a::text').extract()
        #work = response.css(".post-content p::text").extract()[0]
        #tags = response.css('.tags a::text').extract()
        #tags = ','.join(tags)
        pass


