# douban
这是我没事写的一个豆瓣电影top250的爬虫，很幼稚，不过还是能用的，哦呵呵

主要功能：
1 使用BeautifulSoup爬取豆瓣电影top250的主要信息
2 将信息存入本地文本文档之中
3 将信息插入MySQL数据库
  注意编码问题。MySQL只接收python中type为str的变量，不能接收unicode变量（我找了好久才找到的问题）
  解决办法是将变量都encode('utf8')
