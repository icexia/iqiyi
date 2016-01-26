# -*- coding: utf-8 -*-

import scrapy #//import Spider
# from scrapy.selector import Selector
from iqiyi.items import MgtvItem
#//from scrapy import Request
# from twisted.enterprise import adbapi
# import MySQLdb
# import MySQLdb.cursors
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class IqiyiSpider(CrawlSpider):
	name="iqiyi"
	#//allowed_domains=['iqiyi.com']

	#//start_urls=['http://list.iqiyi.com/www/1/-------------4-1-1-iqiyi--.html']

	def __init__(self,rule):
		self.rule=rule
		self.name=rule.spider_name
		self.allowed_domains=rule.allowed_domains
		self.start_urls=rule.start_urls
		rule_list=[]

		rule_list.append(Rule(LinkExtractor(restrict_xpaths=[rule.base_rule]),callback='parse_item'))
		self.rules==tuple(rule_list)
		super(IqiyiSpider,self).__init__()

	# def parse(self,response):
	# 	movies=Selector(response).xpath('//div[@class="wrapper-piclist"]/ul')
	# 	baseUrls=[]
	# 	for movie in movies:
	# 		item=MgtvItem()
	# 		item['url']=movie.xpath('./li/div[@class="site-piclist_pic"]/a/@href').extract()
	# 		baseUrls=item
	# 	for url in baseUrls['url']:
	# 		yield Request(url,callback=self.parseMediaInfo)
			
	def parse_item(self,response):

		item=MgtvItem()
		title=response.xpath(self.rule.title_xpath).extract()
		item['title']=title if title else ""

		eName=response.xpath(self.rule.e_name_xpath).extract()
		item['eName']=eName if  eName else ""

		otherName=response.xpath(self.rule.other_name_xpath).extract()
		item['otherName']=otherName if otherName else ""

		adaptor=response.xpath(self.rule.adaptor_xpath).extract()
		item['adaptor']=adaptor if adaptor else ""
		
		director=response.xpath(self.rule.director_xpath).extract()
		item['director']=director if director else ""
		
		leader=response.xpath(self.rule.leader_xpath).extract()
		item['leader']=leader if leader else ""
			
		kind=response.xpath(self.rule.kind_xpath).extract()
		item['kind']=kind if kind else ""
		
		language=response.xpath(self.rule.language_xpath).extract()
		item['language']=language if language else ""
		
		duration=response.xpath(self.rule.duration_xpath).extract()
		item['duration']=duration if duration else ""
		
		story=response.xpath(self.rule.story_xpath).extract()
		item['story']=story if story else ""
		
		keyWord=response.xpath(self.rule.keyWord_xpath).extract()
		item['keyWord']=keyWord if keyWord else ""
		
		productPerson=response.xpath(self.rule.product_person_xpath).extract()
		item['productPerson']=productPerson if productPerson else ""
		
		dubbing=response.xpath(self.rule.dubbing_xpath).extract()
		item['dubbing']=dubbing if dubbing else ""
		
		executiver=response.xpath(self.rule.executiver_xpath).extract()
		item['executiver']=executiver if executiver else ""

		original=response.xpath(self.rule.original_xpath).extract()
		item['original']=original if original else ""
		
		productColtd=response.xpath(self.rule.productColtd_xpath).extract()
		item['productColtd']=productColtd if productColtd else ""
		
		productionTime=response.xpath(self.rule.production_time_xpath).extract()
		item['productionTime']=productionTime if productionTime else ""
		
		licence=response.xpath(self.rule.licence_xpath).extract()
		item['licence']=licence if licence else ""
		
		registration=response.xpath(self.rule.registration_xpath).extract()
		item['registration']=registration if registration else ""
		
		distributColtd=response.xpath(self.rule.distributColtd_xpath).extract()
		item['distributColtd']=distributColtd if distributColtd else ""
		
		return item