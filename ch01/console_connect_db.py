#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: console_connect_db.py

@time: 2017/11/14 14:26

@desc:   《增加命令行交互的内容》。
        (1) 函数selectByKey，根据用户输入的key，来返回结果。如果存在这个key，返回对应的值（shelves库中保存的对象）。  如果不存在则返回信息告知。 输入空白行退出。
        (2) 函数updateByKey，要求用户输入每个字段的值来更新现存的记录或创建一个新对象。
'''
import shelve

def selectByKey():
    #open the dictionary from shelve files
    db = shelve.open("resources/shelves/class-shelve")




    db.close()


    return ""