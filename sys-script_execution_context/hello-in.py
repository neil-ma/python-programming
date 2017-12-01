#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: hello-in.py

@time: 2017/12/1 10:33

@desc:  os.popen测试输入流，os.popen('','w') 参数为w。
'''

inp = input()
open("resources\\file_re.txt",'w').write("Hello "+ inp + "!\n")


