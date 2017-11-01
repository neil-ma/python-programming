#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: initDB.py

@time: 2017/11/1 18:16

@desc:
'''

dic_tom = {"name":"Tom White","age":39,"sal":900000,"job":"software"}
dic_lily = {"name":"Lily Groove","age":21,"sal":4000,"job":"sale"}
dic_sue = {"name":"Sue Jones","age":47,"sal":1200000,"job":"manager"}

db_01 = {"tom":dic_tom,"lily":dic_lily}
db_01["sue"] = dic_sue;


if __name__ == '__main__':
    for key in db_01.keys():
        print (key,'=>',db_01[key] )

