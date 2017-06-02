#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return theguardian

class theguardian(BaseFeedBook):
    title                 = 'the guardian'
    description           = 'theguardian.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_theguardian.gif"
    coverfile             = "cv_theguardian.jpg"
    oldest_article        = 1
    deliver_days          = ['Monday','Tuesday','Wednesday','Thursday','Friday']

    feeds = [
        ('Top stories', 'http://www.theguardian.com/theguardian/mainsection/topstories/rss'),
        ('UK news', 'http://www.theguardian.com/theguardian/mainsection/uknews/rss'),
        ('International', 'http://www.theguardian.com/theguardian/mainsection/international/rss'),
        ('Eyewitness', 'http://www.theguardian.com/theguardian/mainsection/eyewitness/rss'),
        ('Financial', 'http://www.theguardian.com/theguardian/mainsection/financial3/rss'),
        ('The long read', 'http://www.theguardian.com/theguardian/mainsection/the-long-read/rss'),
        ('Editorials & reply', 'http://www.theguardian.com/theguardian/mainsection/editorialsandreply/rss'),
        ('Comment & debate', 'http://www.theguardian.com/theguardian/mainsection/commentanddebate/rss'),
        ('Reviews', 'http://www.theguardian.com/theguardian/mainsection/reviews/rss'),
        ('Obituaries', 'http://www.theguardian.com/theguardian/mainsection/obituaries/rss'),
        ('Education', 'http://www.theguardian.com/theguardian/mainsection/education/rss'),
        ('Society', 'http://www.theguardian.com/theguardian/mainsection/society/rss'),
        ('Weather', 'http://www.theguardian.com/theguardian/mainsection/weather2/rss'),
        ('Sport', 'http://www.theguardian.com/theguardian/sport/rss'),
        ('G2:Comment & features', 'http://www.theguardian.com/theguardian/g2/features/rss'),
        ('G2:Comment & featuresl', 'http://www.theguardian.com/theguardian/g2/features/rss'),
        ('G2:Arts', 'http://www.theguardian.com/theguardian/g2/arts/rss'),
        ('G2:TV and radio in G2', 'http://www.theguardian.com/theguardian/g2/tvandradio/rss'),
        ]