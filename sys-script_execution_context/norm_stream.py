#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: norm_stream.py

@time: 2017/11/22 13:24

@desc: 标准流
        (1) stream_inter():
            标准流是预先打开的文件对象，在python程序启动时，自动连接到程序上。标准流默认绑定到console上。print和input也是标准输出/输入的接口。
        (2) test_streams():   重定向流：
            a. stdin：默认标准输入的文本从键盘读取。
            b. stdout: 默认的标准输出打印到console窗口。
            c. stderr: 默认向console窗口打印python错误信息。
            命令行通过  python norm_stream.py < resources\\teststream-input.txt > resources\\teststream-output.txt



'''
import sys

def stream_inter():
    print("stdout stream!!")
    print(sys.stdout.write("stdout stream!!"))
    print(input("stdin stream!!>"))
    print("stdin stream!!>")
    print(sys.stdin.readline())

def test_streams():
    print("Hello stream world!")
    while True:
        try: num = input("Enter a number>")
        except:break
        if num:
            print("%d squared is %d" % (int(num),int(num)**2))
        else:
            break
    print("Bye")
if __name__ == '__main__':
    test_streams()