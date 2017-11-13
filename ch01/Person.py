#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: Person.py

@time: 2017/11/10 19:22

@desc:  创建一个简单的person类，
        (1) 定义其属性，提供一个构造方法：
        (2) 添加方法（行为）lastname  giveRaise
        (3) 实现类的继承，Manager继承Person。 Manager.giveRaise()实现多态。
        (4) 重写toString()方法,也就是每个类内置的__str__ 方法。
        (5) 字符串格式打印的使用方式   字符串 % (括号内逗号分隔的多个变量，对应前边的每一个%s)
        (6) 类的__class__ 和 __name__类似对象的反射， instance.__class__ ：The class to which a class instance belongs.   class.__name__ ： The name of the class or type.
        (7) 类的__dict__是一个字典，键是属性名，值为属性值。  字典转String的方法：str(字典)
'''
class Person:
    def __init__(self,name,age,sal=0,job="software"):
        self.name = name
        self.age = age
        self.sal = sal
        self.job = job

    def lastname(self):
        return self.name.split()[0]

    def giveRaise(self,percent):
        self.sal *= (1+percent)

    def __str__(self):
        return str(self.__dict__)



class Manager(Person):
    def __init__(self,name,age,sal=0,job="manager"):
        self.name = name
        self.age = age
        self.sal = sal
        self.job = job

    # instance.method(arg1,arg2)  <=>  class.method(instance,arg1,arg2)  这两种方式等价。
    # 第一种会转化为第二种 通过类来调用时，python会搜索继承树来确定方法所属的类。  <???>
    def giveRaise(self,percent,bonus=0.1):
        Person.giveRaise(self,percent+bonus)

    def __str__(self):
        return "Class: %s ; Name: %s" % (self.__class__.__name__,self.name)

if __name__ == '__main__':
    bob = Person("Bob Fu",54,2300,"manager")
    jack = Person("Jack ton",23,4000,"saler")
    sue = Manager("Sue Brick",45,60000)

    print(bob.lastname())
    print(bob.sal)
    bob.giveRaise(0.2)
    print(bob.sal)

    sue.giveRaise(0.3)
    print(sue)
    print(bob)
