#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: makeDB_shelves_file.py

@time: 2017/11/9 11:51

@desc:   Shelves自动将python对象pickle进和pickle出键访问文件系统。 shelves的访问方法（其自动管理键）。
         因为
'''
import shelve
from ch01.initDB import db_01,dic_lily,dic_sue,dic_tom

# 写入shelves 文件：
shelve_db = shelve.open('resources/shelves/shelves-file')
shelve_db["tom"] = dic_tom
shelve_db["sue"] = dic_sue
shelve_db["lily"] = dic_lily
shelve_db.close()

# 读取shelves 文件，测试时，可以先将上边的写入注释掉。
shelve_ds  = shelve.open('resources/shelves/shelves-file')
print(shelve_ds["tom"])
shelve_ds.close()