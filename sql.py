# -*- coding: utf-8 -*- 

import os

import MySQLdb
import webapp2

connector = MySQLdb.connect(host="localhost", db="sdb", user="root", passwd="32103210", charset="utf8")
cursor = connector.cursor()

sql = u"insert into test_table values('1','python')"
cursor.execute(sql)
sql = u"insert into test_table values('2','パイソン')"
cursor.execute(sql)
sql = u"insert into test_table values('3','ぱいそん')"
cursor.execute(sql)

connector.commit()

cursor.close()
connector.close()
