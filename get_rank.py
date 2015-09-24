#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
import sys

req = urllib2.Request('http://movie.douban.com/subject/1292052/')
content = urllib2.urlopen(req).read().decode("utf-8")
pattern_rank = '<span class="top250-no">No.(\d{1,3})</span>'
pattern_name = '<span property="v:itemreviewed">(.*?)</span>'
pattern_year = '<span class="year">(\(\d{3,4}\))</span>'

name = re.search(pattern_name,content)
#print
#print html.find('itemreviewed')
#print name
#print pattern
print name.group(1)
