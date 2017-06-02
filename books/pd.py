#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return pd

class pd(BaseFeedBook):
    title                 = u'人民日报'
    description           = u'人民网,是世界十大报纸之一。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_pd.gif"
    coverfile             = "cv_pd.jpg"
    oldest_article        = 1
    
    feeds = [
        (u'国内新闻', 'http://www.people.com.cn/rss/politics.xml'),
        (u'国际新闻', 'http://www.people.com.cn/rss/world.xml'),
        (u'经济新闻', 'http://www.people.com.cn/rss/finance.xml'),
        (u'体育新闻', 'http://www.people.com.cn/rss/sports.xml'),
        (u'台湾新闻', 'http://www.people.com.cn/rss/haixia.xml'),
        (u'教育新闻', 'http://www.people.com.cn/rss/edu.xml'),
        (u'强国论坛', 'http://www.people.com.cn/rss/bbs.xml'),
        (u'中文新闻', 'http://www.people.com.cn/rss/opml.xml'),
        ]