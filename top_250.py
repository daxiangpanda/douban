#!/usr/bin/env python
# encoding: utf-8


import urllib
import urllib2
import re

def get_info(content):
    pattern_rank = '<span class="top250-no">No.(\d{1,3})</span>'
    pattern_name = '<span property="v:itemreviewed">(.*?)</span>'
    pattern_year = '<span class="year">(\(\d{3,4}\))</span>'
    name = re.search(pattern_name,content).group(1)
    rank = re.search(pattern_rank,content).group(1)
    year = re.search(pattern_year,content).group(1)
    return rank,name,year
html = ''
for i in range(0,250,25):
    html += (urllib.urlopen('http://movie.douban.com/top250?start=%d&filter=&type=').read())%i

pattern = r'<a href="http://movie.douban.com/subject/\d{7}/">'
tags = re.findall(pattern,html)
for tag in tags:
    url = tag.split('"')[1]
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read().decode("utf-8")
    rank,name,year = get_info(content)
    print year,name,rank
    #print url
#print tags
#print len(tags)
#print len(html)
#for tag in tags:
#    url = tag.split('"')[1]
#    html = urllib.urlopen(url).readline(2)
#    print html
#print html
#print len(urls)
#print len(html)
