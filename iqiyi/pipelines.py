# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
from datetime import datetime
import MySQLdb
import MySQLdb.cursors
import codecs
import json

class MongoDBPipeline(object):
	def __init__(self,dbpool):
		self.dbpool=dbpool

	@classmethod
	def from_settings(cls, settings):
		dbargs = dict(
			host=settings['MYSQL_HOST'],
			db=settings['MYSQL_DBNAME'],
			user=settings['MYSQL_USER'],
			passwd=settings['MYSQL_PWD'],
			charset='utf8',
			cursorclass = MySQLdb.cursors.DictCursor,
			use_unicode= True,
		)
		dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
		return cls(dbpool)
	def process_item(self,item,spider):
		query=self.dbpool.runInteraction(self._mediainfo_insert,item,spider)
		query.addErrback(self.handle_error)

		return item

	def _mediainfo_insert(self,conn,item,spider):
		now=datetime.utcnow()
		if item['title']!='':
			#//conn.execute("insert into MC_MediaInfo(title,leader,kind,source) values('%s,'%s','%s',%s)",item['title'],self.list_format(item['leader']),self.list_format(item['kind']),'爱奇艺')
			# print "insert into MC_MediaInfo(title,eName,otherName,adaptor,director,leader,kind,language,duration,story,keyWord,productPerson,dubbing,executiver,original,productColtd,productionTime,licence,registration,distributColtd,source,createTime)\
			# 	 values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(
			# 		self.list_format(item['title']),
			# 		self.list_format(item['eName']),
			# 		self.list_format(item['otherName']),
			# 		self.list_format(item['adaptor']),
			# 		self.list_format(item['director']),
			# 		self.list_format(item['leader']),
			# 		self.list_format(item['kind']),
			# 		self.list_format(item['language']),
			# 		self.list_format(item['duration']),
			# 		self.list_format(item['story']),
			# 		self.list_format(item['keyWord']),
			# 		self.list_format(item['productPerson']),
			# 		self.list_format(item['dubbing']),
			# 		self.list_format(item['executiver']),
			# 		self.list_format(item['original']),
			# 		self.list_format(item['productColtd']),
			# 		self.list_format(item['productionTime']),
			# 		self.list_format(item['licence']),
			# 		self.list_format(item['registration']),
			# 		self.list_format(item['distributColtd']),
			# 		'爱奇艺',
			# 		now)
			conn.execute(\
				"insert into MC_MediaInfo(title,eName,otherName,adaptor,director,leader,kind,language,duration,story,keyWord,productPerson,dubbing,executiver,original,productColtd,productionTime,licence,registration,distributColtd,source,createTime)\
				 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
					self.list_format(item['title']),
					self.list_format(item['eName']),
					self.list_format(item['otherName']),
					self.list_format(item['adaptor']),
					self.list_format(item['director']),
					self.list_format(item['leader']),
					self.list_format(item['kind']),
					self.list_format(item['language']),
					self.list_format(item['duration']),
					self.list_format(item['story']),
					self.list_format(item['keyWord']),
					self.list_format(item['productPerson']),
					self.list_format(item['dubbing']),
					self.list_format(item['executiver']),
					self.list_format(item['original']),
					self.list_format(item['productColtd']),
					self.list_format(item['productionTime']),
					self.list_format(item['licence']),
					self.list_format(item['registration']),
					self.list_format(item['distributColtd']),
					'爱奇艺',
					now))

	def handle_error(self,e):
		log.err(e)

	def list_format(self,input):
		return ','.join(input)

		
