#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: moreplus.py

@time: 2017/11/29 14:59

@desc: 实现more操作，去掉之前实现的如果stdin重定向为文件时，无法再读取键盘输入的bug。
      (1)假如stdin流被重定向到文件或者管道時，就無法再用它來獲取用戶輸入。如果這時還需要獲取用戶輸入的話，需要使用msvcrt模塊來处理。
        执行语句 python moreplus.py < norm_stream.py
      (2) 需要在命令行测试，不能在pycharm环境正确使用。  脚本有问题。
'''
import sys,os

def get_reply():
    """
    :return:
    """
    # 需要在命令行下调试，pycharm的sys.stdin不是控制台。 sys.stdin.isatty() 为false
    if sys.stdin.isatty():
        print("for test")
        return input("Continue to read? [Y/N]")
    else:
        if sys.platform == 'win32':
            import msvcrt
            #  b'' 代表输入的是bytes而不是str。
            #  msvcrt.putch：Print the byte string char to the console without buffering.
            msvcrt.putch(b'Continue ? [Y/N]')
            # 获取用户输入。
            key = msvcrt.getche()
            msvcrt.putch(b'\n')
            return key
        else:
            # Linux不支持。
            assert False, "Platform doesn't support!"

def more(text,numlines=10):
    """
    :return:
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[0:numlines]
        lines = lines[numlines:]
        for line in chunk:print(line)
        user_input = bytes(get_reply())
        if user_input not in (b'Y',b'y'):
            break

if __name__ == '__main__':
     # more(open("norm_stream.py",encoding='utf-8').read(),10)
     #如果没有参数，直接从console控制台读取。
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open("norm_stream.py", encoding='utf-8').read(), 10)