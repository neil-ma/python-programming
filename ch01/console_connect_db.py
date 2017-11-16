#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: console_connect_db.py

@time: 2017/11/14 14:26

@desc:   《增加命令行交互的内容》。
        (1) 函数selectByKey，根据用户输入的key，来返回结果。如果存在这个key，返回对应的值（shelves库中保存的对象）。  如果不存在则返回信息告知。 输入空白行退出。
        (2) 函数updateByKey，要求用户输入每个字段的值来更新现存的记录或创建一个新对象。
        (3) getattr() : Return the value of the named attribute of object. getattr(x, 'foobar') is equivalent to x.foobar.
            ljust(): Return a copy of the object left justified in a sequence of length width. 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
'''
import shelve
from ch01.Person import Person

def selectByKey():
    #Fixed attributes of the object:
    field_names = ('name','age','job','sal')
    # 为了格式化输出数据。
    max_lenth = max(len(field_len) for field_len in field_names)
    #open the dictionary from shelve files . the db contains three persons, they are  bob sue jack
    db = shelve.open("resources/shelves/class-shelve")
    while True:
        user_input=input("Key? =>")
        if not user_input:
            break
        if db.__contains__(user_input):
            #Get the Person object
            person = db[user_input]
            for field in field_names:
                print(field.ljust(max_lenth),'=>',getattr(person,field))
        else:
            print("No such key \""+user_input+"\"!","")
    db.close()


def updateByKey():
    # 如果输入了不存在的键，直接新增这个person。
    # Fixed attributes of the object:
    field_names = ('name', 'age', 'job', 'sal')
    db = shelve.open("resources/shelves/class-shelve")
    while True:
        key=input("Key? =>")
        if not key:
            break
        if db.__contains__(key):
            #如果存在取出对象
            person = db[key]
        else:
            # 如果不存在创建新对象（name是?）
            person = Person("?",0,0,"")
        for field in field_names:
            attr_new = input('[%s]=%s\n\t\tnew?=>'%(field,getattr(person, field)))
            setattr(person, field, attr_new)
            db[key] = person
    db.close()

if __name__ == "__main__":
    #selectByKey()
    # updateByKey()
    db = shelve.open("resources/shelves/class-shelve")
    for key in db:
        print(db[key])
    db.close()