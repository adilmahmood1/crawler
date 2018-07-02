# -*- coding: utf-8 -*-
import scrapy
from caseblocks.items import CaseblocksItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
	
	
class Spider1Spider(CrawlSpider):
	name = 'spider1'
	allowed_domains = ['caseblocks.com']
	start_urls = ['http://caseblocks.com/']
	download_delay = 0.3 #300ms of delay
	
	rules = (Rule (LinkExtractor(), callback="parse_obj", follow=True),)
	
	def parse_obj(self, response):
		item = CaseblocksItem()
		item['url'] = response.url
		item['title'] = response.xpath("//head/title/text()").extract()
		item['http'] = response.status
		
		return item