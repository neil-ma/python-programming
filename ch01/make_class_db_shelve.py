#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: make_class_db_shelve.py

@time: 2017/11/13 16:23

@desc: 将内存中的类，shelve 成文件。  shelve核心就是 键-值 管理的文件，这里边值是对象，键是字符串。 db['bob'] = bob(object)
'''
import shelve
from ch01.Person import Person,Manager

bob = Person("Bob Fu",54,2300,"manager")
jack = Person("Jack ton",23,4000,"saler")
sue = Manager("Sue Brick",45,60000)

db = shelve.open("resources/shelves/class-shelve")
db['bob'] = bob
db['jack'] = jack
db['sue'] = sue
db.close()

db_update = shelve.open("resources/shelves/class-shelve")
bob.age = 35
bob.giveRaise(0.5)
db_update['bob'] = bob
db_update.close()

db_select = shelve.open("resources/shelves/class-shelve")
print(db_select["bob"])
db_select.close()