#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: format-file.py

@time: 2017/11/16 18:49

@desc: 《格式化文档》
      Python中大多数系统级接口都在两个模块中 os 和 sys。 还包括 glob，socket，threading，_thread，subprocess等等一些module。
      sys负责导出与Python解释器本身相关的组件。os包含与Python所在底层操作系统相对应的变量和函数。
      (1) module_test ：概览os和sys module
          dir()简单返回一个列表，包含了带属性对象的所有属性的字符串名称。
      (2) 实现more功能，
      (3) 常用的字符串方法：
'''
import os,sys

def module_test():
    print ("os模块包含有%s个属性；sys模块包含有%s个属性。"%(len(dir(os)),len(dir(sys))))

if __name__ == '__main__':
    module_test()