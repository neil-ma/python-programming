#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: command_args.py

@time: 2017/11/22 13:23

@desc: 命令行参数
    （1） 以字典key-value形式返回，命令行参数。 例如 -i oits  字典中增加 {'-i','oits'}
        地板除法： 除法不管操作数为何种数值类型，总是会舍去小数部分   //
'''
import sys


def usage():
    print("You input error arguments. Usage: python xx.py -i XXX -s XXX")

def getopts():
    args = sys.argv
    length = args.__len__()
    dics = {}
    if length % 2 == 0 or length == 1:
        usage()
    else:
        for i in range(0,length//2):
            if "-" in args[i*2+1]:
                dics[args[i*2+1]] = args[i*2+2]
            else:
                usage()
    return dics

if __name__ == '__main__':
    print(getopts())





