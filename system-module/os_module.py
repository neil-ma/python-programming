#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: os_module.py

@time: 2017/11/16 18:49

@desc:   (1)os.path的常用的方法
         (2) 在脚本中运行 shell （Linux shell / Windows BatchCommand ）
            os.system： 在python脚本中运行shell命令；os.popen ： 运行命令并且与其输入/输出流相连。
'''
import os,subprocess

def os_info():
    #获得进程号
    print(os.getpid())
    #打印当前目录
    print(os.getcwd())
    os.chdir(r'C:\Users')
    print(os.getcwd())

# pathsep：目录列表中分割目录的符号；sep：目录组分隔符；pardir：父目录；curdir：当前目录；linesep：行分隔符，在windows中是回车换行\r\n。
print(os.pathsep,os.sep,os.pardir,os.curdir,os.linesep)

#os.path提供了一整套目录处理的工具。包括os.path.isfile,os.path.isdir,os.path.exists,os,path.getsize
#如果文件不存在，os.path.isfile,os.path.isdir会返回False。
print(os.path.isfile(r'C:\Users'),os.path.isdir(r'C:\Users'),os.path.exists(r'C:\Users'),os.path.getsize(r'C:\Users') )

#os.path.split将文件名从目录路径中剥离出来。os.path.splitext：剥离了文件的扩展名 os.path.join则是合并起来。
file_abs_path = r"C:\Windows\twain.dll"
print("原始文件路径：",file_abs_path)
print("os.path.split =>" , os.path.split(file_abs_path))
print("os.path.splitext =>" , os.path.splitext(file_abs_path))
print("os.path.join =>" , os.path.join(r"C:\Windows","twain.dll"))

# os.path.dirname 路径目录       os.path.basename文件名称
print("os.path.dirname =>" , os.path.dirname(file_abs_path))
print("os.path.basename =>" , os.path.basename(file_abs_path))

#如果路径需要混用windows和linux，可以使用os.path.normpath ；
print("os.path.normpath =>" , os.path.normpath(file_abs_path))
print("os.path.abspath =>" , os.path.abspath(r"resources\apache_log"))

# 末尾的返回值0表示，命令已经成功执行了。 os.system，直接调用shell命令。
def shell_dispose():
    os.system('dir .')
    os.system('type __init__.py')

#os.popen除了可以执行shell命令外，还可以连接到命令的标准输入/输出流。
# os.popen("shell") 将返回一个类似文件的对象。默认与输出流相连，如果提供参数'w'，则与输入流相连。
def shell_get_stdout():
    text = os.popen("type resources/apache_log").read()
    print(text)
    ls = os.popen("dir .").readlines()
    print(ls)


#subprocess 模块可以实现与os.system,os.popen相同功能，但是代码更加复杂，但是对流的连接和使用提供更完整控制。
#subprocess的 call方法与os.system功能差不多。但是在执行 Windows下的shell内建命令需要额外协议（例如type）  If shell is True, the specified command will be executed through the shell.
#在Unix平台，当shell设置为False时，程序命令行由os.execvp运行。在Windows下，需要将shell=True传给call，这样能够运行shell内建命令。
# To support a wide variety of use cases    使用popen方法
# 将Python文件作为程序运行和导入程序文件来使用其中的函数是截然不同的做法，一般后者要比前者快。
# os.startfile是新增的一个函数，这个函数会打开一个文件，就像是用鼠标单击其图标一样。
def sub_process_using():
    text = subprocess.call('type sys_module.py', shell=True)
    print(text)
    popen_case = subprocess.Popen('type sys_module.py', shell=True, stdout=subprocess.PIPE)
    # communicate执行命令  如果不用commnicate，直接使用popen_case.stdout.read()也可以，将标准输出读出。
    print(popen_case.communicate())
    # print(popen_case.stdout.read())
    print(popen_case.returncode)
    os.startfile(r'D:\Program\sts-3.9.1.RELEASE\STS')

if __name__ == '__main__':
    sub_process_using()