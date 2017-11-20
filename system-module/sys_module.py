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

       (1) sys.path: 是一个目录的列表，指定模块的搜索路径。
       (2) sys.modules：是一个字典。


'''
import sys,traceback
#介绍关于sys.path变量
def sys_path():
    print(sys.path)
    #sys.path初始化自环境变量PYTHONPATH，并且可以修改。但是对sys.path的修改不是永久的，在python进程关闭后失效。
    sys.path.append(r"D:\My_Own\music")
    print(sys.path)

def sys_module():
    # Python会话或者程序导入的每一个模块，在sys.modules字典中都有一个 name:module项
    # 例如：'os': <module'os'from'D: \\Programes\\python-3.5.2\\lib\\os.py'>
    print(sys.modules)

def sys_exception():
    #sys模块中的一些属性，为我们提供最近抛出的python异常的相关信息。
    #sys.exc_info()会返回一个元组，包含异常的类型、值和追踪对象。 traceback模块
    try:
        raise TypeError("value define error!!")
    except:
        exc_info = sys.exc_info()
        print(exc_info)
        print(exc_info[0])
        print(exc_info[1])
        print(traceback.print_tb(exc_info[2]))


if __name__ == '__main__':
    # str_method_test()
    # print(sys.platform,sys.maxsize,sys.version)
    # sys_path()
    # sys_module()
    sys_exception()