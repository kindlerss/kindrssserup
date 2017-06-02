#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return independent

class independent(BaseFeedBook):
    title                 = 'the Independent'
    description           = 'The Independent is a British national morning newspaper published in London by Independent Print Limited, owned by Alexander Lebedev since 2010.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ti.gif"
    coverfile             = "cv_ti.jpg"
    oldest_article        = 1
    
    feeds = [
        ('News - UK', 'http://www.independent.co.uk/news/uk/?service=rss'),
        ('News - World', 'http://www.independent.co.uk/news/world/?service=rss'),
        ('News - Business', 'http://www.independent.co.uk/news/business/?service=rss'),
        ('News - People', 'http://www.independent.co.uk/news/people/?service=rss'),
        ('News - Science', 'http://www.independent.co.uk/news/science/?service=rss'),
        ('News - Education', 'http://www.independent.co.uk/news/education/?service=rss'),
        ('Opinion', 'http://www.independent.co.uk/opinion/?service=rss'),
        ('Environment', 'http://www.independent.co.uk/environment/?service=rss'),
        ('Sport - Athletics', 'http://www.independent.co.uk/sport/general/athletics/?service=rss'),
        ('Sport - Football', 'http://www.independent.co.uk/sport/football/?service=rss'),
        ('Sport - Olympics', 'http://www.independent.co.uk/sport/olympics/?service=rss'),
        ('Life & Style - Fashion', 'http://www.independent.co.uk/life-style/fashion/?service=rss'),
        ('Life & Style - Health and Families', 'http://www.independent.co.uk/life-style/health-and-families/?service=rss'),
        ('Life & Style - History', 'http://www.independent.co.uk/life-style/history/?service=rss'),
        ('Arts & Ents - Architecture', 'http://www.independent.co.uk/arts-entertainment/architecture/?service=rss'),
        ('Travel', 'http://www.independent.co.uk/travel/?service=rss'),
        ('Money', 'http://www.independent.co.uk/money/?service=rss'),
        ]