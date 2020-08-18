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

class BanglaBdnewsTSpider(CrawlSpider):
    name = 'bangla_bdnews'
    allowed_domains = ['bangla.bdnews24.com']
    start_urls = ['https://bangla.bdnews24.com/']

    rules = (
        Rule(LinkExtractor(allow='/article[0-9]{1,}', ), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/[a-z]{1,}'), follow=True)
    )

    def parse_item(self, response):
        uid = response.url.split("/")[4]
        title = response.xpath('///*[@id="news-details-page"]/h1/text()').getall()
        doc_type = "Title"
        category = response.url.split("/")[3]
        parsed_uri = urlparse(response.url)
        rootdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        publishdate = response.xpath('//*[@id="article_notations"]/p/span[2]/text()').extract()
        parsetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item = utils.return_items(uid, title, doc_type, category, parsed_uri, rootdomain, publishdate, parsetime)
        yield item