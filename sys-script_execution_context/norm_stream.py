#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: norm_stream.py

@time: 2017/11/22 13:24

@desc: 标准流
        (1) stream_inter():  标准流：
            标准流是预先打开的文件对象，在python程序启动时，自动连接到程序上。标准流默认绑定到console上。print和input也是标准输出/输入的接口。
        (2) test_streams():   重定向流：
            a. stdin：默认标准输入的文本从键盘读取。
            b. stdout: 默认的标准输出打印到console窗口。
            c. stderr: 默认向console窗口打印python错误信息。
            在unix和windows中，命令行通过： python norm_stream.py < resources\\teststream-input.txt > resources\\teststream-output.txt
        (3) test_pipe():  通过管道连接程序：
            命令行执行：python norm_stream.py < resources\\teststream-input.txt | more
        (4) sorter()和adder()是自实现的2个函数，可以通过管道多次传送。
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

def sorter():
    lines = sys.stdin.readlines()
    lines.sort()
    for i in lines: print(i,end='')

def adder():
    sum = 0
    while True:
        # try:data = input()             # 最基本的实现方式，通过input()获取输入。
        data=sys.stdin.readline()        # input()也是输入流接口，所以使用stdin.readline()也可以逐行处理。 使用stdin.readline()不用担心处理异常，
                                         # 因为数据在stdin文件对象中，不会遇到 EOFError: EOF when reading a line
        # except:break
        if data:
            sum += int(data)
        else:
            break
    print(sum,end='')
    return sum

# 使用在file对象上迭代的方式。在file对象上迭代，for循环每次自动抓取一行。
def adder_senior():
    sum = 0
    for line in sys.stdin: sum += int(line)      # 直接int sys.stdin的迭代即可。
    print(sum,end='')
    return sum

if __name__ == '__main__':
    adder_senior()