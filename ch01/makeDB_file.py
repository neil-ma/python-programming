#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: makeDB_file.py

@time: 2017/11/1 19:19

@desc:  将内存的中一个DB（字典构成）落地成文件， 将一个文件读入内存。
'''

databasefilename = 'resources/persons-file'
ENDRECORD='endrec.'
ENDDB='enddb.'
SEPERATE='=>'

dic_tom = {"name":"Tom White","age":39,"sal":900000,"job":"software"}
dic_lily = {"name":"Lily Groove","age":21,"sal":4000,"job":"sale"}
dic_sue = {"name":"Sue Jones","age":47,"sal":1200000,"job":"manager"}

db_01 = {"tom":dic_tom,"lily":dic_lily}
db_01["sue"] = dic_sue;

#loadDatabase ： 将文件中的数据load到内存中的数据库对象。

#storeDatabase : 将内存中的数据库 持久化到文件上
def storeDatabase(db,databasefilename = databasefilename):
    dbfile=open(databasefilename,'w')
    for key in db.keys():
        print(key,file=dbfile)
        for key1 in db[key].keys():
            print(key1,SEPERATE,db[key][key1],file=dbfile)
        print(ENDRECORD,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()

if __name__ == '__main__':
    storeDatabase(db_01,databasefilename)


