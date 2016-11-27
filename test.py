#!/usr/bin/python
# coding: UTF-8
 
# 書き込む文字列
str = """ I'll be puzzled about what I should do from now on."""
 
f = open('text.txt', 'w') 
f.write(str) 
f.close() 
