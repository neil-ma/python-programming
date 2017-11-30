#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: redirect_object.py

@time: 2017/11/29 19:09

@desc: 数据流重定向到python对象。
        在脚本内部将sys.stdin和sys.stdout重置到文件类的对象。任何在方法上与文件类似（实现接口）的对象都可以充当标准流。
'''