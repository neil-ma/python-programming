#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: makeDB_file.py

@time: 2017/11/1 19:19

@desc:  将内存的中一个DB（字典构成）落地成文件， 将一个文件读入内存。 格式可以参考 resources/standard 下的person-files
'''

from ch01.initDB import  db_01

databasefilename = 'resources/standard/persons-file'
ENDRECORD='endrec.'
ENDDB='enddb.'
SEPERATE='=>'


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


#loadDatabase ： 将文件中的数据load到内存中的数据库对象。
def loadDatabase(databasefilename):
    dbfile = open(databasefilename,'r')
    db_rec = {}
    db = {}
    personName = ""
    while True:
        fileline = dbfile.readline().replace('\n','')     #读一行数据
        if not fileline:
            break
        if fileline == ENDDB:
            dbfile.close()
            return db
        elif fileline == ENDRECORD:
            db[personName] = db_rec
            # 需要重新创建一个新的db_rec对象，之前的程序错误，没有这步，导致后边db的每一个key的value都改成了这个值（最后出现的值）：
            #{'tom': {'age': '47', 'job': 'manager', 'sal': '1200000', 'name': 'Sue Jones'}, 'lily': {'age': '47', 'job': 'manager', 'sal': '1200000', 'name': 'Sue Jones'}, 'sue': {'age': '47', 'job': 'manager', 'sal': '1200000', 'name': 'Sue Jones'}}
            #这也就表名，在字典的每一个value，虽然我们觉得保存的是当时的db_rec，实际上也是db_rec指向的一个对象，如果db_rec不重新初始化一个的话。会全部修改。
            db_rec = {}
        else:
            if fileline.__contains__(SEPERATE):
                (name_raw,value_raw)=fileline.split(SEPERATE)
                # 生成的文件中有空格（print函数所致），例如： age => 21 ，如果从文件载入内存的字典，需要去空格
                (name,value) = (name_raw.strip(),value_raw.strip())
                db_rec[name] = value
            else:
                personName = fileline


if __name__ == '__main__':
    storeDatabase(db_01,databasefilename)
    # loadDbFile = "resources/standard/persons-file-forload"
    # db  = loadDatabase(loadDbFile)
    # print(db)


