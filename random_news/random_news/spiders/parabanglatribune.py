# -*- coding: utf-8 -*-
import requests
import scrapy
from random import randrange
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule 
import utils
import requests 
import json
from urllib.parse import urlparse
import datetime

class BanglatribunePSpider(CrawlSpider):
    name = 'banglatribune'
    allowed_domains = ['www.banglatribune.com']
    start_urls = ['http://www.banglatribune.com/']

    rules = (
        Rule(LinkExtractor(allow='/news/', ), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/[a-z]{1,}'), follow=True)
    )
    def parse_item(self, response):
        uid = response.url.split("/")[5]
        title = response.xpath('//p/text()').getall()[randrange(4)]
        doc_type = "Paragraph"
        category = response.url.split("/")[3]
        parsed_uri = urlparse(response.url)
        rootdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        publishdate = response.xpath('//*[@class="time"]/@data-published').extract()
        parsetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item = utils.return_items(uid, title, doc_type, category, parsed_uri, rootdomain, publishdate, parsetime)
        if(category!="others"):
            yield item