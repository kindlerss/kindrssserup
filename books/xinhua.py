#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return xinhua

class xinhua(BaseFeedBook):
    title                 = u'新华网'
    description           = u'创办于1997年11月，是新华通讯社主办的中央重点新闻网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xinhua.gif"
    coverfile             = "cv_xinhua.jpg"
    oldest_article        = 1
    
    feeds = [
        (u'时政频道', 'http://www.xinhuanet.com/politics/news_politics.xml'),
        (u'国际频道', 'http://www.xinhuanet.com/world/news_world.xml'),
        (u'地方联播', 'http://www.xinhuanet.com/local/news_province.xml'),
        (u'军事频道', 'http://www.xinhuanet.com/mil/news_mil.xml'),
        (u'台湾频道', 'http://www.xinhuanet.com/tw/news_tw.xml'),
        (u'华人频道', 'http://www.xinhuanet.com/overseas/news_overseas.xml'),
        (u'金融频道', 'http://www.xinhuanet.com/finance/news_finance.xml'),
        (u'财经频道', 'http://www.xinhuanet.com/fortune/news_fortune.xml'),
        (u'房产频道', 'http://www.xinhuanet.com/house/news_house.xml'),
        (u'法制频道', 'http://www.xinhuanet.com/legal/news_legal.xml'),
        (u'教育频道', 'http://www.xinhuanet.com/edu/news_edu.xm'),
        (u'体育频道', 'http://www.xinhuanet.com/sports/news_sports.xml'),
        (u'娱乐频道', 'http://www.xinhuanet.com/ent/news_ent.xml'),
        (u'汽车频道', 'http://www.xinhuanet.com/auto/news_auto.xml'),
        (u'旅游频道', 'http://www.xinhuanet.com/travel/news_travel.xml'),
        (u'科技频道', 'http://www.xinhuanet.com/tech/news_tech.xml'),
        (u'出国频道', 'http://www.xinhuanet.com/abroad/news_abroad.xml'),
        (u'食品频道', 'http://www.xinhuanet.com/food/news_food.xml'),
        (u'健康频道', 'http://www.xinhuanet.com/health/news_health.xml'),
        (u'书画频道', 'http://www.xinhuanet.com/shuhua/news_calligraphy.xml'),
        (u'能源频道', 'http://www.xinhuanet.com/energy/news_energy.xml'),
        (u'民航频道', 'http://www.xinhuanet.com/air/news_air.xml'),
        ]