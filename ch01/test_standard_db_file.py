#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: test_standard_db_file.py

@time: 2017/11/3 17:48

@desc: 测试 makeDB_file中的laod和makeDB方法。
       1.同级路径import的问题。  引用makeDB_file module中的loadDatabase，使用报错。
       同级目录module直接import之前有报错： SystemError: Parent module '' not loaded, cannot perform relative import

'''

from .makeDB_file import loadDatabase,storeDatabase
db = loadDatabase("resources/standard/persons-file")
print(db["lily"]["name"])
