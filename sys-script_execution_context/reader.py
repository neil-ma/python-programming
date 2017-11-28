#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: reader.py

@time: 2017/11/28 15:00

@desc:　测试管道
        管道测试cmd ：　python writer.py | python reader.py
        使用管道连接了2个程序，这是一种简单的跨程序通信的方式。
        sys.stdin.readline() 和sys.stdin.readlines() 的区别。
        A. readline() :　This is a sentence Testing from command line!!!
        B. readlines(): ['This is a sentence Testing from command line!!!\n', '45\n']
'''

import sys
#调用了input()一次，所以读出了第一行。
print("Got first line: \"",input(),"\"")
# print("Got second line: \"",input(),"\"")
data = int(sys.stdin.readline()[:-1])
print("Simple Calculation: %d multiply 2 is : %d" % (data,data*2))

# print(sys.stdin.readlines())