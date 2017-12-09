#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: redirect_object.py

@time: 2017/11/29 19:09

@desc:  (1)数据流重定向到python对象。
        在脚本内部将sys.stdin和sys.stdout重置到文件类的对象。任何在方法上与文件类似（实现接口）的对象都可以充当标准流。
        a.提供类似文件read方法的对象可以指定给sys.stdin，以从该对象的read方法读取输入。
        b.提供类似文件write方法的对象可以指定给sys.stdout，所有的标准输出将发送到该对象方法上。

        (2) io.StringIO 和io.BytesIO工具类
        StringIO :  An in-memory stream for text I/O. The text buffer is discarded when the close() method is called.
        StringIO经常被用来作为字符串的缓存，应为StringIO有个好处，他的有些接口和文件操作是一致的，也就是说用同样的代码，可以同时当成文件操作或者StringIO操作。
        BytesIO与StringIO类似，是一个字节缓冲流的实现。

        (3) print调用中的重定向。

        (4) popen_subprocess_re() ：
            os.popen和子进程重定向  ： 效果类似shell的重定向流到程序的命令行管道语法。对脚本所启动程序的流进行重定向，而非重定向脚本本身的流。
            通过传入不同的模式标志，可以在调用的脚本中重定向一个 子程序的输入或输出流到文件。
        A. class subprocess.Popen  : Execute a child program in a new process.
        B. os.popen : Open a pipe to or from command cmd. The return value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'.
'''
import io,sys,os,subprocess

class Output():
    """

    """

def stringio_testing():
    """
    io.StringIO类，缓冲字符串测试。
    :return:
    """
    # write向缓冲字符串写入内容，getvalue()直接转换为string
    string_io = io.StringIO()
    string_io.write("spam\n")
    string_io.write("json\n")
    print("测试1：\n",string_io.getvalue())

    string_io2 = io.StringIO("janus\nfunction\ngsl")
    print("测试2：\n",string_io2.readline())
    print(string_io2.readline())
    print(string_io2.readline())

def stringio_re_stdout():
    buff = io.StringIO()
    #backup
    temp = sys.stdout
    sys.stdout = buff
    print(56,"google\nibm\namazon")
    sys.stdout = temp
    print(buff.getvalue())

def print_re():
    f = open("resources\\file_re.txt",'w')
    # print重定向到文件
    print("janus-log",file=f)

    buff = io.StringIO()
    # print 重定向到String缓冲流
    print("Kafka", file=buff)
    print("Python", file=buff)
    print("Scala", file=buff)
    # print正常定向 stdout
    print(buff.getvalue())

def popen_re():
    inp = input()
    # 文件对象直接write，写入文件
    open("resources\\file_re.txt",'w').write("Hello " + inp +"!\n")

    # os.popen执行时，默认的模式是'r'，也就是标准输出。如果修改模式'r'为'w'就会变为标准输入了。
    pipe = os.popen("type writer.py")
    print(pipe.read())
    print(pipe.close())

    # 输入流由 pipe.write()来写入。
    pipe1 = os.popen("python hello-in.py","w")
    pipe1.write("Glums")
    pipe1.close()

def subprocess_re():
    #使用subprocess，可以使用2种方法来调用 subprocess.call() , subprocess.Popen
    # (1) call方法
    X = subprocess.call("python cwd.py")
    print(X)
    # (2) subprocess.Popen  commnicate方式
    #  Popen.communicate  :Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.
    # communicate() returns a tuple (stdout_data, stderr_data).
    pipe = subprocess.Popen("python cwd.py",stdout=subprocess.PIPE)
    print("communicate()方式：",pipe.communicate())
    # (3) subprocess.Popen  read方式
    pipe2 = subprocess.Popen("python cwd.py", stdout=subprocess.PIPE)
    print("pipe.stdout.read()方式：",pipe2.stdout.read())
    #退出状态。  Wait for child process to terminate. Set and return returncode attribute.
    print("pipe.stdout.read()方式：",pipe2.wait())

    #(4) 提供输入参数：
    pipe3 = subprocess.Popen("python hello-in.py", stdin=subprocess.PIPE)
    pipe3.stdin.write(b"IBM")
    pipe3.stdin.close()
    pipe3.wait()



if __name__ == '__main__':
    # stringio_testing()
    # stringio_re_stdout()
    # print_re()
    # popen_re()
    subprocess_re()