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
        I. 'a'模式表示追加，'+'表示支持读写（之前只能单纯的读或者写）
        II.   open(文件名,打开模式,缓存策略)
            打开模式 ： w+ 打开文件并读写 ,  r+  打开文件并读写 ,  a+  打开文件并读添
            缓存策略 ： 控制文件的缓冲，数据在传输之前的队列方式，以便提高性能。 0: 无缓冲，数据立即传输，只允许在二进制下进行。1：逐行缓冲。其他正值表示全缓冲（默认值）

       (5) 二进制和文本文件：
       python把文本模式文件当做unicode来处理，并自动在输入时对文件解码，在输出时，对文件编码。
        >>> open('file-directory-tools\\resources\\data_file_4read').read()
        'Hadoop\nSolr\nHive\nHbase\nKafka'
        >>> open('file-directory-tools\\resources\\data_file_4read','rb').read()
        b'Hadoop\r\nSolr\r\nHive\r\nHbase\r\nKafka'

        (6) bin_parse_pack(): struct模块：
        struct模块用于打包和解压二进制数据的调用。

        (7) random_access():  文件的随机读取：
         因为文本文件需要unicode编码解码，所以，二进制文件更加适合于随机读取，使用 file.seek()来定位。

        (8) os模块中的底层文件工具，
        相比于open()工具，os中基于描述符的文件工具更低层且更复杂，一般情况下还是使用open()更多，os.open()少得多。
        I. fileno()
        文件对象方法fileno返回的整数描述符是与某个内建文件对象想关联的。 sys.stdin 0 ; sys.stdout 1; sys.stderr 2
        fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。
        II. fdopen()把文件描述符封装进文件对象。

        (9)其他os模块文件工具。
        os.rename()重命名文件; os.remove()删除文件; os.chown()修改文件所有者 ; os.chmod()修改文件权限。
        os.stat()返回一个数值组成的元组（关于文件的底层信息，一般os.stat()比较少用），

'''

import struct,os,sys

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

def bin_parse_pack():
    #使用struct模块来打包和解析二进制文件
    # pack的第一个参数是，进行pack和unpack的format string，详细内容参考mannul。
    data =struct.pack('hhl', 1, 2, 3)
    file = open("resources\\bin.txt",'wb')
    file.write(data)
    file.close()

    data_text = open("resources\\bin.txt").read()
    data_bin = open("resources\\bin.txt","rb").read()
    data_unpact = struct.unpack('hhl',data_bin)
    print("文本读取内容：",data_text)
    print("二进制unpack后读取：",data_unpact)

def random_access():
    file = open("resources\\random_access.bin","w+b")
    test_str = b'spam'
    w1 = b'X' * 8
    w2 = b'Y' * 8
    data = b''
    for c in test_str: data += bytes([c])*8
    file.write(data)
    file.seek(0)
    print("初始化字符读取：",file.read())
    file.seek(0)
    file.write(w1)
    # 写入是覆盖写，会覆盖之前开头的8个s。注意变化。
    file.seek(0);print("开头写入8个X：",file.read())
    # seek(16) 是从文件"绝对开始"的位置起，向后位移16位。
    file.seek(len(w1)*2);file.write(w2)
    file.seek(0);print("从第3个字节开始写入8个Y：",file.read())

def os_file():
    #sys.stdin, sys.stdout, sys.stderr 对应的整数描述符
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        print(stream.fileno())

    sys.stdout.write("Hello sys stdout!!!\n")
    #fd=1代表stdout， os.write第二个参数必须是bytes
    os.write(1,b"os.write(): Hello sys stdout!!!\n")

    # os模块为文件处理提供了更多底层控制。
    file_os = open("resources\\os_file.txt",'w')
    #获得文件描述符  3
    fd = file_os.fileno()
    os.write(fd,b'insert with os.write(fd,str)!!')
    file_os.flush()
    file_os.close()

    #相比于内建的open，更加灵活。 以 读-写 或者 二进制模式打开一个基于描述符的文件。
    file_os_open = os.open("resources\\data_file_4read",(os.O_RDWR | os.O_BINARY))
    print(os.read(file_os_open,10))
    #os.lseek(fd, pos, how)   how参数 0：从头开始偏移  1：从当前位置偏移  2：相对于文件尾部偏移。
    #回到首部
    os.lseek(file_os_open,0,0)
    print(os.read(file_os_open, 50))

    os.lseek(file_os_open, 0, 0)
    os.write(file_os_open,b'HELLO')

    #把文件描述符封装进文件对象。
    file_os_obj =os.open("resources\\data_file_4read",(os.O_RDWR | os.O_BINARY))  #file_os_obj=3
    objfile = os.fdopen(file_os_obj,'rb')
    print(objfile.read(100))
    objfile.close()
    #在文本模式下，读取和写入将执行unicode编码和换行符转换。
    file_os_obj1 = os.open("resources\\data_file_4read", (os.O_RDWR | os.O_BINARY))  # file_os_obj1=3
    objfile1 = os.fdopen(file_os_obj1, 'r')
    print(objfile1.read(100))
    objfile1.close()
    #当然是用内建的open()函数来封装文件描述符也是完全可以的。
    file_os_obj2 = os.open("resources\\data_file_4read", (os.O_RDWR | os.O_BINARY))  # file_os_obj2=3
    objfile2=open(file_os_obj2,'r')
    print(objfile2.read())
    objfile2.close()

def os_tools():
    #创建测试文件
    file = open("resources\\file_test",'w')
    file.write("hello niu")
    file.close()
    os.rename("resources\\file_test","resources\\file_test.txt")
    #删除文件
    os.remove("resources\\file_test.txt")
    info = os.stat("resources\\file_test.txt")
    #os.stat_result(st_mode=33206, st_ino=18014398509669407, st_dev=4068484812, st_nlink=1, st_uid=0, st_gid=0, st_size=9, st_atime=1513154972, st_mtime=1513154972, st_ctime=1513154972)
    print(info)
    print(info.st_mode,info.st_size)
    import stat
    print(info[stat.ST_MODE],info[stat.ST_SIZE])
    print("stat模块方法：",stat.S_ISDIR(info[stat.ST_MODE]),stat.S_ISREG(info[stat.ST_MODE]))
    # 替代os.stat的方式， os.path模块就可以完成
    path = "resources\\file_test.txt"
    print("os.path模块方法：",os.path.isdir(path),os.path.isfile(path),os.path.getsize(path))


if __name__ == "__main__":
    # close_file()
    # read_files()
    # other_open_options()
    # bin_parse_pack()
    # random_access()
    # os_file()
    os_tools()