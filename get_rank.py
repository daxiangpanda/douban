#!/usr/bin/env python
# encoding: utf-8

import urllib
import re

html = urllib.urlopen(r'http://movie.douban.com/subject/1292052/').read()
pattern = r'<span property="v:itemreviewed">([a-zA-Z\u4E00-\u9FA5\s]+)</span>'

rank = re.findall(pattern,html)
print rank
