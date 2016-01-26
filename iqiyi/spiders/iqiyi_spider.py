# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from iqiyi.items import MgtvItem
from scrapy import Request
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class IqiyiSpider(Spider):
	name="iqiyi"
	allowed_domains=['iqiyi.com']
	start_urls=['http://list.iqiyi.com/www/1/-------------4-1-1-iqiyi--.html']

	def parse(self,response):
		movies=Selector(response).xpath('//div[@class="wrapper-piclist"]/ul')
		baseUrls=[]
		for movie in movies:
			item=MgtvItem()
			item['url']=movie.xpath('./li/div[@class="site-piclist_pic"]/a/@href').extract()
			baseUrls=item
		for url in baseUrls['url']:
			yield Request(url,callback=self.parseMediaInfo)
			
	def parseMediaInfo(self,response):

		#//items=[]
		item=MgtvItem()
		title=Selector(response).xpath('//div[@class="title"]/div[@class="textOverflow"]/a/text()').extract()
		if len(title)>0:
			item['title']=title
		else:
			item['title']=''
		eName=Selector(response).xpath('//div[@class="title"]/div[@class="textOverflow"]/a/text()').extract()
		if len(eName)>0:
			item['eName']=eName
		else:
			item['eName']=''

		otherName=Selector(response).xpath('//div[@class="title"]/div[@class="textOverflow"]/a/text()').extract()
		if len(otherName)>0:
			item['otherName']=otherName
		else:
			item['otherName']=''
		adaptor=Selector(response).xpath('//div[@class="title"]/div[@class="textOverflow"]/a/text()').extract()
		if len(adaptor)>0:
			item['adaptor']=adaptor
		else:
			item['adaptor']=''
		director=Selector(response).xpath('//div[@class="title"]/div[@class="textOverflow"]/a/text()').extract()
		if len(director)>0:
			item['director']=director
		else:
			item['director']=''
		leader=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(leader)>0:
			item['leader']=leader
		else:
			item['leader']=''	
		kind=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(kind)>0:
			item['kind']=kind
		else:
			item['kind']=''
		language=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(language)>0:
			item['language']=language
		else:
			item['language']=''	
		duration=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(duration)>0:
			item['duration']=duration
		else:
			item['duration']=0
		story=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(story)>0:
			item['story']=story
		else:
			item['story']=''
		keyWord=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(keyWord)>0:
			item['keyWord']=keyWord
		else:
			item['keyWord']=''
		productPerson=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@id="datainfo-actor"]/span[@class="type-con"]/a/text()').extract()
		if len(productPerson)>0:
			item['productPerson']=productPerson
		else:
			item['productPerson']=''
		dubbing=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(dubbing)>0:
			item['dubbing']=dubbing
		else:
			item['dubbing']=''
		executiver=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(executiver)>0:
			item['executiver']=executiver
		else:
			item['executiver']=''
		original=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(original)>0:
			item['original']=original
		else:
			item['original']=''
		productColtd=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(productColtd)>0:
			item['productColtd']=productColtd
		else:
			item['productColtd']=''
		productionTime=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(productionTime)>0:
			item['productionTime']=productionTime
		else:
			item['productionTime']=''
		licence=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(licence)>0:
			item['licence']=licence
		else:
			item['licence']=''
		registration=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(registration)>0:
			item['registration']=registration
		else:
			item['registration']=''
		distributColtd=Selector(response).xpath('//div[@class="jiemu-people pr"]/p[@class="type-tag"]/span[@class="type-con"]/a/text()').extract()
		if len(distributColtd)>0:
			item['distributColtd']=distributColtd
		else:
			item['distributColtd']=''
		
		return item