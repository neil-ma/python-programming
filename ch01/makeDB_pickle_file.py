#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: makeDB_pickle_file.py

@time: 2017/11/8 18:10

@desc: 1. 使用pickle文件 将任意Python类型的数据转化成可以保存在文件中的格式。 需要引入pickle module
       2. glob module的使用：
        The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
'''
import pickle,glob
from ch01.initDB import db_01

if __name__ == '__main__':
    # 写入内存的DB数据到磁盘（pickle方式），因为pickle是二进制方式，文件对象open时，使用wb模式。
    # 这也是序列化过程   Python对象  -->  二进制字节流
    dbfile_w=open('resources/pickle/person-file-pickle','wb')
    db_01['tom']['age'] = 98
    pickle.dump(db_01,dbfile_w)
    dbfile_w.close()

    # 读取二进制文件到python对象， 反序列化  pickle文件格式。
    dbfile_r = open('resources/pickle/person-file-pickle','rb')
    db_02 = pickle.load(dbfile_r)
    print(db_02)
    dbfile_r.close()

    # 字典中的每一条记录放一个pickle文件。
    rec_file_name = ""
    for rec in db_01.keys():
        rec_file_name='resources/pickle/'+rec+'.pcl'
        rec_file_w = open(rec_file_name,'wb')
        pickle.dump(db_01[rec],rec_file_w)
        rec_file_w.close()

    # 使用glob module来批量获取所有pickle文件，读取整个库
    for pickle_file in glob.glob('resources/pickle/*.pcl'):
        rec_file_r = open(pickle_file,'rb')
        print(pickle.load(rec_file_r))
        rec_file_r.close()

    # 改变某一条记录：
