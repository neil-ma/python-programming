#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: sys_module.py

@time: 2017/11/19 13:39

@desc: 介绍sys模块。
       Python模块很多，学习模块的一个方法是，在IDLE中 help(sys)，会提供一个module reference 然后学习，也可以使用 Python Manuals
       MODULE REFERENCE
                https://docs.python.org/3.6/library/sys


'''

import sys

if __name__ == '__main__':
    # str_method_test()
    print(sys.platform,sys.maxsize,sys.version)