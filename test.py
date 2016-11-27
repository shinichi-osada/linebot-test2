#!/usr/bin/python
# coding: UTF-8
 
# 書き込む文字列
str = """ I'll be puzzled about what I should do from now on."""
 
f = open('text.txt', 'w') # 書き込みモードで開く
f.write(str) # 引数の文字列をファイルに書き込む
f.close() # ファイルを閉じる
