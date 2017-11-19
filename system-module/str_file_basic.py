#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: str_file_basic.py

@time: 2017/11/19 12:19

@desc: (1)str_method_test() : 介绍常见的字符串函数的使用。
       字符串是str模块，str.find()等。还有一个string标准库模块。
       find，replace，in，strip,lower,isalpha,split,join
        Python不会自动将字符串转换为整型，反之亦然。需要自己转换

       (2)file_test(),open方法返回文件对象，该对象是python的核心。
        文件对象的read()方法，读取文件中的内容。 read()方法读出的部分，就不在文件对象中了。下边的测试。如果str1 执行读出文件所有的内容
        后边的几个字符串就是空值了。
        写文件的方法，参考 ch01/makeDB_file.py

'''

def str_method_test():
    mystr = "grooveXXXgithubXXXjanusXXXapache"
    #如果find不到字符串，则返回-1。
    print("XXX子字符串第一个匹配所在的偏移位置：",mystr.find("XXX"))
    #replace函数返回的新串，原有的字符串mystr不会改变。字符串在python中是不可变的。
    print("替换XXX为SPAM:",mystr.replace("XXX","SPAM"))
    print(mystr)

    # str in str   返回True False>>
    print("XXX是否在mystr中？","XXX" in mystr)
    print("XXXF是否在mystr中？", "XXXF" in mystr)
    # strip去掉首尾空格
    # str.strip(args) 去掉首部和尾部的字符，注意args会每一个单个字符在首部、尾部匹配，然后去掉。如果args是空，默认去掉空字符。
    print("去掉首尾的X和g字符：",mystr.strip("Xg"))
    print("去掉首尾空行：","    chips    ".strip())

    print(mystr.lower())
    print(mystr.isalpha())

    #split函数如果参数为空，默认是使用空格来split
    print(mystr.split("XXX"))
    print("aaa  bbb ccc".split())
    my_str_list = mystr.split("XXX")

    #需要注意的是join是string的方法，所以在参数中，添加一个list，而不是list.join(string)
    print("NI".join(my_str_list))

    #list()方法将一个字符串转换成字符列表。
    my_chars = list(mystr)
    print(my_chars)

    # str ->  int      int , eval
    print(int("42"),eval("43"))
    # int -> str       str , repr
    print(str(42)+'a',repr(43)+'3')

def file_test():
    file = open("resources/apache_log")

    #将后边N个字节读取为字符串
    str1 = file.read(5)
    #跨过换行读取下一行
    str2 = file.readline()
    #将整个文件读取为单行字符串组成的列表
    str3 = file.readlines()
    # 将整个文件读取为字符串
    str4 = file.read()

    print(str1,str2,str3,str4)
    file.close()

if __name__ == '__main__':
    # str_method_test()
    file_test()