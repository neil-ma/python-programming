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
          help 是PyDoc系统提供的接口之一，Python自带的标准代码库，可以呈现对象相关文档。在交互界面常用，查看帮助。
      (2) 实现more功能，一个文本，每次读取n行。
          splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的"列表"，
          如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

      (3) 常用的字符串方法：
'''
import os,sys

def module_test():
    print ("os模块包含有%s个属性；sys模块包含有%s个属性。"%(len(dir(os)),len(dir(sys))))
    print(sys.__doc__)
    help(sys)

def more(text,line_num=15):
    lines = text.splitlines()
    while True:
        display_lines = lines[:line_num]
        other_lines = lines[line_num:]
        if len(display_lines) > 0 :
            print(display_lines)
        if len(display_lines) > 0 and input("continue? [y/n]") == 'y':
            lines = other_lines
        else:
            break

def string_method_testing():
    return ""

if __name__ == '__main__':
    module_test()
    # more(sys.__doc__)