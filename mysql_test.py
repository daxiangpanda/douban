#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'root',
        db = 'test1'
        )
cur = conn.cursor()

#create table
#cur.execute("create table movie(rak int,name varchar(50),year year,intro varchar(1000),score float);")
 
cur.execute("insert into movie3 values('1','肖申克的救赎 The Shawshank Redemption','1994','9.6','　　20世纪40年代末，小有成就的青年银行家安迪')")
def insert(info):
    cur.execute("insert into movie3 values(%s,%s,%s,%s,%s)",info)
    for i in info:
        print type(i)
info = ['2','肖申克的救赎 The Shawshank Redemption','1994','9.6','　　20世纪40年代末，小有成就的青年银行家安迪']
insert(info)
cur.close()
conn.commit()
conn.close()

