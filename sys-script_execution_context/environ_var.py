#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: environ_var.py

@time: 2017/11/22 13:24

@desc: 环境变量
      （1）查看系统环境变量 get_shell()。Python在启动时候有一些变量被预设，例如PYTHONPATH.
          I. sys.path是运行期的实际模块搜索路径，它会合并PYTHONPATH的值到当前路径的后边。
          II. pythonpath是
        (2) 修改shell变量 update_shell(): 对os.environ 键的赋值，内部会调用os.putenv，它负责修改Python解释器外部的shell变量
            shell变量的设置会传递给子进程，而永远都不会传到父进程。
            需要谨记一点：在程序中对shell变量的修改只对程序本身及它衍生的子程序有效。
'''
import os,sys
def get_shell():
    envs = os.environ.keys()
    envs_list =list(os.environ.keys())
    java_path = os.environ['JAVA_HOME']

    pythonpath = os.environ['PYTHONPATH'].split(os.pathsep)
    for srcpath in pythonpath:
        print(srcpath)
    print(envs_list,java_path,pythonpath,sys.path[:4],sep = "\n")

def update_shell():
    # Python的最顶层程序（environ_var.py）退出后，USERNAME变量会变回初始值。
    print(os.environ['USERNAME'])
    os.environ['USERNAME'] = 'WHITE'
    os.system("python D:\\V-learning\\PyCharmWorkSpace\\python-programming\\sys-script_execution_context\\cwd.py")
    print(os.environ['USERNAME'])


if __name__ == '__main__':
    # get_shell()
    update_shell()

