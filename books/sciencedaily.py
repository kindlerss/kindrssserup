#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return sciencedaily

class sciencedaily(BaseFeedBook):
    title                 = 'Science Daily'
    description           = 'Breaking science news and articles on global warming.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_sciencedaily.gif"
    coverfile             = "cv_sciencedaily.jpg"
    oldest_article        = 7
    
    feeds = [
        ('Top News', 'http://www.sciencedaily.com/rss/top.xml'),
        ('Top Science', 'http://www.sciencedaily.com/rss/top/science.xml'),
        ('Top Health', 'http://www.sciencedaily.com/rss/top/health.xml'),
        ('Top Technology', 'http://www.sciencedaily.com/rss/top/technology.xml'),
        ('Top Environment', 'http://www.sciencedaily.com/rss/top/environment.xml'),
        ('Top Society', 'http://www.sciencedaily.com/rss/top/society.xml'),
        ('Strange & Offbeat', 'http://www.sciencedaily.com/rss/strange_offbeat.xml'),
	('Most Popular', 'http://www.sciencedaily.com/rss/most_popular.xml'),
	('Health & Medicine', 'http://www.sciencedaily.com/rss/health_medicine.xml'),
        ]