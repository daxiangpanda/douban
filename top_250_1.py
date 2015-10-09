#!/usr/bin/env python
# encoding: utf-8


import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def get_info(content):
    soup = BeautifulSoup(content)
    rank = soup.find('span','top250-no').get_text().split('.')[1]
    name = soup.find('span',property="v:itemreviewed").get_text()
    year = soup.find('span','year').get_text()[1:5]
    try:
        intro = soup.find('span','all hidden').get_text().replace(' ','')
    except:
        intro = soup.find_all(property="v:summary")[0].get_text().replace(' ','')
    intro = intro.replace(r'\n','')
    score = soup.find('strong','ll rating_num').get_text()
    return rank,name,year,score,intro
f = open(r'/home/ted/python/douban/豆瓣top250.txt','w+')
for i in range(0,250,25):
    html = (urllib.urlopen('http://movie.douban.com/top250?start=%d&filter=&type='%i).read()).replace('\n','')
    #html = html.replace(' ','')
    pattern = r'<a href="http://movie.douban.com/subject/\d{7}/">'
    tags = re.findall(pattern,html)
    for tag in tags:
        url = tag.split('"')[1]
        req = urllib2.Request(url)
        try:
            content = urllib2.urlopen(req).read().decode("utf-8")
        except urllib2.URLError,e:
            f.write('你寻找的电影不存在，错误码'+str(e.code))
        rank,name,year,score,intro = get_info(content)
        s = "电影排名：" + rank + "名称:" + name + "上映时间:" + year + "评分" + score + "\n" + "intro:" + intro
        print "已写入" + s
        f.write(s)
f.close()
