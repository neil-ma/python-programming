#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: test_standard_db_file.py

@time: 2017/11/3 17:48

@desc: 测试 makeDB_file中的laod和makeDB方法。
       1.同级路径import的问题。  引用makeDB_file module中的loadDatabase，使用报错。
       同级目录module直接import之前有报错： SystemError: Parent module '' not loaded, cannot perform relative import
       2. 问题解决方式： 在from ... import ... 语句中，需要写出module文件的绝对路径。 例如下边例子，需要写ch01.makeDB_file(这个问题困扰了好久)
       3.官方的解释doc： Note that relative imports are based on the name of the current module.
       Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.
       4.类型转换 ：

'''
from ch01.makeDB_file import loadDatabase,storeDatabase
db = loadDatabase("resources/standard/persons-file")
print("从文件中读出的信息：")
print(db)
#所有人涨薪 50% 后，更新文件。
for person_name in db.keys():
    db[person_name]["sal"] = 1.5 * float(db[person_name]["sal"])
print("涨薪后的信息：")
print(db)
print("写入文件：")
storeDatabase(db)