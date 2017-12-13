#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: commands.py

@time: 2017/12/13 17:45

@desc:  行处理函数
'''
from Scanner import scanner,scanner_map

def processline(line):
    if line[0] == '*':
        pro_line = 'Mr.' + line[1:]
    elif line[0] == '+':
        pro_line = 'Ms.' + line[1:]
    else:
        pro_line = line
    print(pro_line)

if __name__ == "__main__":
    scanner("resources\\hillbillies",processline)
    scanner_map("resources\\hillbillies", processline)