#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return theDailyMirror

class theDailyMirror(BaseFeedBook):
    title                 = 'The Daily Mirror'
    description           = 'The Daily Mirror is a British national daily Left Wing tabloid newspaper founded in 1903. It is owned by parent company Trinity Mirror. '
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_tdm.gif"
    coverfile             = "cv_tdm.jpg"
    oldest_article        = 7
    
    feeds = [
        ('UK News', 'http://www.mirror.co.uk/news/uk-news/rss.xml'),
        ('world News', 'http://www.mirror.co.uk/news/world-news/rss.xml'),
        ('Sports', 'http://www.mirror.co.uk/sport/rss.xml'),
        ('3AM', 'http://www.mirror.co.uk/3am/rss.xml'),
        ('Lifestyle', 'http://www.mirror.co.uk/lifestyle/rss.xml'),
        ]