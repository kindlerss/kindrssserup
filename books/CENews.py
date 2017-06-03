#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return CENews

class CENews(BaseFeedBook):
    title                 = u'双语新闻'
    description           = u'双语新闻选取了China Daily，FT双语栏目，以及其他双语新闻。'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_CENews.gif"
    coverfile             = "cv_CENews.jpg"
    oldest_article        = 7
    
    feeds = [
        (u'FT双语阅读', 'http://www.ftchinese.com/rss/diglossia'),
        (u'中国日报|双语', 'http://www.chinadaily.com.cn/rss/lt_rss.xml'),
        (u'爱语吧|双语', 'http://feed43.com/3865665266733664.xml'),
        ]