#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: makeDB_file.py

@time: 2017/11/1 19:19

@desc:  将内存的中一个DB（字典构成）落地成文件， 将一个文件读入内存。 格式可以参考 resources/standard 下的person-files
'''

databasefilename = 'resources/standard/persons-file'
ENDRECORD='endrec.'
ENDDB='enddb.'
SEPERATE='=>'


dic_tom = {"name":"Tom White","age":39,"sal":900000,"job":"software"}
dic_lily = {"name":"Lily Groove","age":21,"sal":4000,"job":"sale"}
dic_sue = {"name":"Sue Jones","age":47,"sal":1200000,"job":"manager"}

db_01 = {}
db_01["tom"]= dic_tom;
db_01["lily"]=dic_lily;
db_01["sue"] = dic_sue;

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
        if fileline != ENDRECORD and fileline != ENDDB:
            if fileline.__contains__(SEPERATE):
                (name,value)=fileline.split(SEPERATE)
                db_rec[name] = value
                #print (db_rec)
            else:
                personName = fileline
        elif fileline == ENDDB:           #ENDDB 到了文件末尾，关闭文件句柄，返回db。
            print("To the end of file!!")
            dbfile.close()
            return db
        else:                #读到了 ENDRECORD  把这批字典加到db中去。
            db[personName] = db_rec

if __name__ == '__main__':
    #storeDatabase(db_01,databasefilename)
    loadDbFile = "resources/standard/persons-file-forload"
    db  = loadDatabase(loadDbFile)
    print(db)


