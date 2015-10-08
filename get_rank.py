#!/usr/bin/env python
# encoding: utf-8

import urllib2
from bs4 import BeautifulSoup


req = urllib2.Request('http://movie.douban.com/subject/1292052/')
content = urllib2.urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(content)
rank = soup.find('span','top250-no').get_text()[3]
name = soup.find('span',property="v:itemreviewed").get_text()
year = soup.find('span','year').get_text()
intro = soup.find('span','all hidden').get_text().replace(' ','')
intro = intro.replace(r'\n','')
score = soup.find('strong','ll rating_num').get_text()
intro
#intro = re.search(pattern_intro,content.decode('utf8'),re.DOTALL)
#print
#print html.find('itemreviewed')
#print name
#print pattern_name

print name,rank,year,intro,score
