#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: Scanner.py

@time: 2017/12/13 17:20

@desc: 通用函数，扫描一个文件，并对每一行应用函数function
       name: 文件路径。
       function: 应用的通用函数。
'''
def scanner(name,function):
    file = open(name,'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line.replace("\n",""))

#使用内建map函数的更精简解决办法：
def scanner_map(name,function):
    list(
        map(function,open(name,'r'))         #也使用了文件迭代器， 对name文件的每一行，使用map，也就是function来清洗。
    )