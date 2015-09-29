#!/usr/bin/env python
# encoding: utf-8


import urllib
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def get_info(content):
    pattern_rank = '<span class="top250-no">No.(\d{1,3})</span>'
    pattern_name = '<span property="v:itemreviewed">(.*?)</span>'
    pattern_year = '<span class="year">(\(\d{3,4}\))</span>'
    pattern_score = '<strong class="ll rating_num" property="v:average">(\d\.\d)</strong>'
    pattern_intro = '<span property="v:summary">(.*?)</span>'
    name = re.search(pattern_name,content).group(1)
    rank = re.search(pattern_rank,content).group(1)
    year = re.search(pattern_year,content).group(1)
    score = re.search(pattern_score,content).group(1)
    intro = re.search(pattern_intro,content).group(1)
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
        s = "电影排名：" + rank + "名称:" + name + "上映时间:" + year + "评分" + score + "\n"
        b = intro
        print "已写入" + s
        f.write(s)
        f.write(b)
f.close()
