#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return usatoday

class usatoday(BaseFeedBook):
    title                 = 'USA Today'
    description           = 'USA Today is a national American daily middle-market newspaper published by the Gannett Company. It was founded by Al Neuharth on September 15, 1982.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_usatoday.gif"
    coverfile             = "cv_usatoday.jpg"
    oldest_article        = 7
    
    feeds = [
        ('Top Headlines', 'http://rssfeeds.usatoday.com/usatoday-NewsTopStories'),
        ('Tech Headlines', 'http://rssfeeds.usatoday.com/usatoday-TechTopStories'),
        ('Personal Tech', 'http://rssfeeds.usatoday.com/UsatodaycomTech-PersonalTalk'),
        ('Science', 'http://rssfeeds.usatoday.com/TP-ScienceFair'),
        ('Health', 'http://rssfeeds.usatoday.com/UsatodaycomHealth-TopStories'),
        ('Travel Headlines', 'http://rssfeeds.usatoday.com/UsatodaycomTravel-TopStories'),
        ('Money Headlines', 'http://rssfeeds.usatoday.com/UsatodaycomMoney-TopStories'),
        ('Entertainment Headlines', 'http://rssfeeds.usatoday.com/usatoday-LifeTopStories'),
        ('Sport Headlines', 'http://rssfeeds.usatoday.com/UsatodaycomSports-TopStories'),
        ('Weather Headlines', 'http://rssfeeds.usatoday.com/usatoday-WeatherTopStories'),
        ('Most Popular', 'http://rssfeeds.usatoday.com/Usatoday-MostViewedArticles'),
        ('Offbeat News', 'http://rssfeeds.usatoday.com/UsatodaycomOffbeat-TopStories'),
        ]