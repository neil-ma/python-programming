#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: os_module.py

@time: 2017/11/16 18:49

@desc:   (1)os.path的常用的方法
         (2) 在脚本中运行 shell （Linux shell / Windows BatchCommand ）
'''
import os

def os_info():
    #获得进程号
    print(os.getpid())
    #打印当前目录
    print(os.getcwd())
    os.chdir(r'C:\Users')
    print(os.getcwd())

# pathsep：目录列表中分割目录的符号；sep：目录组分隔符；pardir：父目录；curdir：当前目录；linesep：行分隔符，在windows中是回车换行\r\n。
print(os.pathsep,os.sep,os.pardir,os.curdir,os.linesep)

#os.path提供了一整套目录处理的工具。包括os.path.isfile,os.path.isdir,os.path.exists,os,path.getsize
#如果文件不存在，os.path.isfile,os.path.isdir会返回False。
print(os.path.isfile(r'C:\Users'),os.path.isdir(r'C:\Users'),os.path.exists(r'C:\Users'),os.path.getsize(r'C:\Users') )

#os.path.split将文件名从目录路径中剥离出来。os.path.splitext：剥离了文件的扩展名 os.path.join则是合并起来。
file_abs_path = r"C:\Windows\twain.dll"
print("原始文件路径：",file_abs_path)
print("os.path.split =>" , os.path.split(file_abs_path))
print("os.path.splitext =>" , os.path.splitext(file_abs_path))
print("os.path.join =>" , os.path.join(r"C:\Windows","twain.dll"))

# os.path.dirname 路径目录       os.path.basename文件名称
print("os.path.dirname =>" , os.path.dirname(file_abs_path))
print("os.path.basename =>" , os.path.basename(file_abs_path))

#如果路径需要混用windows和linux，可以使用os.path.normpath ；
print("os.path.normpath =>" , os.path.normpath(file_abs_path))
print("os.path.abspath =>" , os.path.abspath(r"resources\apache_log"))