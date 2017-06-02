#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return TheWashingtonPost

class TheWashingtonPost(BaseFeedBook):
    title                 = 'the Washington Post'
    description           = 'Leading source for news, video and opinion on politics.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_twp.gif"
    coverfile             = "cv_twp.jpg"
    oldest_article        = 7
    
    feeds = [
        ('World', 'http://feeds.washingtonpost.com/rss/world'),
        ('National', 'http://feeds.washingtonpost.com/rss/national'),
        ('White House', 'http://feeds.washingtonpost.com/rss/politics/whitehouse'),
        ('Business', 'http://feeds.washingtonpost.com/rss/business'),
        ('Opinions', 'http://feeds.washingtonpost.com/rss/opinions'),
        ('Investigations', 'http://feeds.washingtonpost.com/rss/investigations'),
        ('Local', 'http://feeds.washingtonpost.com/rss/local'),
        ('Entertainment', 'http://feeds.washingtonpost.com/rss/entertainment'),
        ('Sports', 'http://feeds.washingtonpost.com/rss/sports'),
        ('Redskins', 'http://feeds.washingtonpost.com/rss/sports/redskins'),
        ('Special Reports', 'http://feeds.washingtonpost.com/rss/national/special-reports'),
        ]