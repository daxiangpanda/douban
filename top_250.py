#!/usr/bin/env python
# encoding: utf-8

#
import urllib
import re
html = ''
for i in range(0,250,25):
    html += (urllib.urlopen('http://movie.douban.com/top250?start=%d&filter=&type=').read())%i

pattern = r'<a href="http://movie.douban.com/subject/\d{7}/">'
tags = re.findall(pattern,html)
for tag in tags:
    url = tag.split('"')[1]
    print url
print tags
print len(tags)
print len(html)
#for tag in tags:
#    url = tag.split('"')[1]
#    html = urllib.urlopen(url).readline(2)
#    print html
#print html
#print len(urls)
#print len(html)
