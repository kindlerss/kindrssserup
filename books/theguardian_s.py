#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return theguardian_s

class theguardian_s(BaseFeedBook):
    title                 = 'the guardian Saturday'
    description           = 'theguardian Saturday.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_theguardian.gif"
    coverfile             = "cv_theguardian.jpg"
    oldest_article        = 1
    deliver_days          = ['Saturday']

    feeds = [
        ('Top stories', 'http://www.theguardian.com/theguardian/mainsection/topstories/rss'),
        ('UK news', 'http://www.theguardian.com/theguardian/mainsection/uknews/rss'),
        ('International', 'http://www.theguardian.com/theguardian/mainsection/international/rss'),
        ('Saturday', 'http://www.theguardian.com/theguardian/mainsection/saturday/rss'),
        ('Editorials & reply', 'http://www.theguardian.com/theguardian/mainsection/editorialsandreply/rss'),
        ('Comment & debate', 'http://www.theguardian.com/theguardian/mainsection/commentanddebate/rss'),
        ('Financial', 'http://www.theguardian.com/theguardian/mainsection/financial3/rss'),
        ('Money', 'http://www.theguardian.com/theguardian/mainsection/money/rss'),
        ('Obituaries', 'http://www.theguardian.com/theguardian/mainsection/obituaries/rss'),		
        ('Reviews', 'http://www.theguardian.com/theguardian/mainsection/reviews/rss'),
        ('Weather', 'http://www.theguardian.com/theguardian/mainsection/weather2/rss'),       
        ('Sport', 'http://www.theguardian.com/theguardian/sport/rss'),
        ('Guardian review', 'http://www.theguardian.com/theguardian/guardianreview/rss'),
        ('Travel', 'http://www.theguardian.com/theguardian/travel/rss'),		
        ('Weekend:Starters', 'http://www.theguardian.com/theguardian/weekend/starters/rss'),
        ('Weekend:Features', 'http://www.theguardian.com/theguardian/weekend/features2/rss'),
        ('Weekend:Body & mind', 'http://www.theguardian.com/theguardian/weekend/body-and-mind/rss'),
        ('Weekend:Fashion and beauty', 'http://www.theguardian.com/theguardian/weekend/fashion-and-beauty/rss'),
        ('Weekend:Food and drink', 'http://www.theguardian.com/theguardian/weekend/food-and-drink/rss'),
        ('Weekend:Space', 'http://www.theguardian.com/theguardian/weekend/space2/rss'),
        ('Weekend:Back', 'http://www.theguardian.com/theguardian/weekend/back/rss'),
        ('The Guide:Features', 'http://www.theguardian.com/theguardian/theguide/features/rss'),
        ('The Guide:Previews', 'http://www.theguardian.com/theguardian/theguide/reviews/rss'),
        ('The Guide:TV & radio', 'http://www.theguardian.com/theguardian/theguide/tv-radio/rss'),
        ('Cook', 'http://www.theguardian.com/theguardian/cook/rss'),
        ('Special supplement', 'http://www.theguardian.com/theguardian/special-supplement/rss'),
        ]