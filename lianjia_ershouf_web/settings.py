# -*- coding: utf-8 -*-
BOT_NAME = 'lianjia_ershouf_web'

SPIDER_MODULES = ['lianjia_ershouf_web.spiders']
NEWSPIDER_MODULE = 'lianjia_ershouf_web.spiders'


#CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 1.5
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
COOKIES_ENABLED = False


#DOWNLOADER_MIDDLEWARES = {
#    'lianjia_ershouf_web.middlewares.LianjiaErshoufWebDownloaderMiddleware': 543,
#}


ITEM_PIPELINES = {
   'lianjia_ershouf_web.pipelines.MongoPipeline': 300,
}


MONGO_URI = 'localhost'
MONGO_DATABASE = 'lianjia'
