# -*- coding: utf-8 -*-

# Scrapy settings for iqiyi project
## -*- coding: utf-8 -*-
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iqiyi'

SPIDER_MODULES = ['iqiyi.spiders']
NEWSPIDER_MODULE = 'iqiyi.spiders'

DOWNLOAD_DELAY = 2
 
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

ITEM_PIPELINES=['iqiyi.pipelines.MongoDBPipeline', ]
MYSQL_HOST="10.1.201.152"
MYSQL_DBNAME="MediaCloud"
MYSQL_USER='root'
MYSQL_PWD='@@$iere05923*&($'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iqiyi (+http://www.yourdomain.com)'
