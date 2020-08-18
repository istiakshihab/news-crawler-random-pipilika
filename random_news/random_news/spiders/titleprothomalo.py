# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule 
import utils
import requests 
import json
from urllib.parse import urlparse
import datetime

# uid, comment, doc_type, category, url, rootdomain, publishdate, parsetime, source="newspaper",datadomain=""

class ProthomAloTSpider(CrawlSpider):
    name = 'prothomalo'
    allowed_domains = ['prothomalo.com']
    start_urls = ['https://prothomalo.com/']

    rules = (
        Rule(LinkExtractor(allow='/article/', ), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/[a-z]{1,}'), follow=True)
    )

    
    def parse_item(self, response):
        uid = response.url.split("/")[5]
        title = response.xpath('//div[@class="right_title"]/h1/text()').getall()
        doc_type = "Title"
        category = response.xpath('//*[@class="secondary_logo"]/a/span/text()').getall()[0]
        parsed_uri = urlparse(response.url)
        rootdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        publishdate = response.xpath('//div[@class="time each_row"]/span[1]/@content').extract()
        parsetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item = utils.return_items(uid, title, doc_type, category, parsed_uri, rootdomain, publishdate, parsetime)
        yield item