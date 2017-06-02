#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return theobserver

class theobserver(BaseFeedBook):
    title                 = 'the observer'
    description           = 'the observer.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_theobserver.gif"
    coverfile             = "cv_theobserver.jpg"
    oldest_article        = 1
    deliver_days          = ['Sunday']

    feeds = [
        ('News', 'http://www.theguardian.com/theobserver/news/uknews/rss'),
        ('Comment', 'http://www.theguardian.com/theobserver/news/comment/rss'),
        ('World news', 'http://www.theguardian.com/theobserver/news/worldnews/rss'),
        ('In focus', 'http://www.theguardian.com/theobserver/news/focus/rss'),
        ('Business', 'http://www.theguardian.com/theobserver/news/business/rss'),
        ('Cash', 'http://www.theguardian.com/theobserver/news/cash/rss'),
        ('Observer Sport', 'http://www.theguardian.com/theobserver/sport/rss'),
        ('The New Review:Agenda', 'http://www.theguardian.com/theobserver/new-review/agenda/rss'),
        ('The New Review:Features', 'http://www.theguardian.com/theobserver/new-review/features/rss'),
        ('The New Review:Discover', 'http://www.theguardian.com/theobserver/new-review/discover/rss'),
        ('The New Review:Critics', 'http://www.theguardian.com/theobserver/new-review/critics/rss'),
        ('The New Review:Books', 'http://www.theguardian.com/theobserver/new-review/books/rss'),
        ('Observer Magazine:Regulars', 'http://www.theguardian.com/theobserver/magazine/regulars/rss'),
        ('Observer Magazine:Life & style', 'http://www.theguardian.com/theobserver/magazine/life-and-style/rss'),
        ('Observer Magazine:Features', 'http://www.theguardian.com/theobserver/magazine/features2/rss'),
        ('Special supplement', 'http://www.theguardian.com/theobserver/special-supplement/rss'),
        ('Observer Food Monthly', 'http://www.theguardian.com/theobserver/foodmonthly/rss'),
        ]