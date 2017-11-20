#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: os_module.py

@time: 2017/11/16 18:49

@desc: 
'''
import os

# pathsep：目录列表中分割目录的符号；sep：目录组分隔符；pardir：父目录；curdir：当前目录；linesep：行分隔符，在windows中是回车换行\r\n。
print(os.pathsep,os.sep,os.pardir,os.curdir,os.linesep)

#os.path提供了一整套目录处理的工具。包括os.path.isfile,os.path.isdir,os.path.exists,os,path.getsize
print(os.path.isfile(r'C:\Users'),os.path.isdir(r'C:\Users'),os.path.exists(r'C:\Users'),os.path.getsize(r'C:\Users') )

