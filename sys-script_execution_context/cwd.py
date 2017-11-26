#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: cwd.py

@time: 2017/11/22 13:23

@desc: 当前工作路径
      一个脚本总是启动于CWD，而非它所在的目录。反之，import永远首先搜索文件所在目录，而非CWD（除非CWD=脚本所在目录）,Python自动将脚本所在目录添加到模块搜索路径的最前。
      例如在一个目录下，执行python dir/dir/exam.py  脚本所在目录 != CWD

'''
import os, sys

def whereami_test():
    print("os.getcwd => ", os.getcwd())
    print("sys.path => ", sys.path[:6])


if __name__ == '__main__':
    whereami_test()
