#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: file_tools.py

@time: 2017/12/4 10:10

@desc:  文件工具：
     (1) 文本文件还有UNICODE字符串，二进制文件包含原始8位字节（二进制文件内容为字节字符串）:
        str字符串总是代表unicode文本、而bytes和bytearray字符串代表二进制数据。 文本文件自动执行换行符转换，而且自动将unicode编码应用于文件内容（编码+换行符转换）。

     （2）确认文件关闭， close_file():

     （3）读取文件内容，read_files():
        file.seek(0)  在file.read()读取时，读取了所有文件内容，文件游标已经到了尾部，若在重新读取，需要执行seek(0) 重新到文件首部。
        文件迭代器：　　for line in  myfile :  每次会读取一行。

      (4) 其他打开选项， other_open_options():
        I. 'a'模式表示追加，
        II.   open(文件名,打开模式,缓存策略)
            打开模式 ： w+ 打开文件并读写 ,  r+  打开文件并读写 ,  a+  打开文件并读添
            缓存策略 ： 控制文件的缓冲，数据在传输之前的队列方式，以便提高性能。 0: 无缓冲，数据立即传输，只允许在二进制下进行。1：逐行缓冲。其他正值表示全缓冲（默认值）

       (5) 二进制和文本文件：
        

'''

def close_file():
    #传统异常处理器模式，来保证文件对象关闭。常用方法
    file = open("resources\\file_tool.txt","w")
    try:
        file.write("Glum  Bingos!!!")
    finally:
        file.close()

    #上下文管理器方式： with仅应用于支持上下文管理器协议的对象
    with open("resources\\file_tool.txt","r") as file:
        print(file.read())


def read_files():
    with open("resources\\data_file_4read","r") as myfile:
        #一次读出所有内容到一个字符串
        print(myfile.read())

        # 一次读出所有内容到一个字符串列表：
        myfile.seek(0)
        lines = myfile.readlines()
        print(lines)

        # 一次读出前边几个字符：
        myfile.seek(0)
        print("一次读出前边几个字符：",myfile.read(8))

        # 一次读出一行：
        myfile.seek(0)
        print("一次读出一行：",myfile.readline())

        #文件迭代器。 文件迭代器不是一次性加载到行列表，因此处理大文件时，可以节省空间。
        print("文件迭代器：")
        myfile.seek(0)
        for line in myfile:
            print(line)

def other_open_options():
    file_append = open("resources\\file_tool.txt","a")
    file_append.write("AloneSo")
    file_append.close()


if __name__ == "__main__":
    # close_file()
    # read_files()
    other_open_options()