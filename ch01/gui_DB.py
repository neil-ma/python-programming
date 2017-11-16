#!/usr/bin/env python

# encoding: utf-8
'''

@author: natty

@file: gui_DB.py

@time: 2017/11/14 14:34

@desc:   《GUI图形界面管理DB》
       Python有很多GUI工具包或者构建器，如tkinter、wxPython、PyQt、PythonCard、Dabo 等。其中tkinter是Python自带的，标准的。支持跨平台
       创建gui程序的步骤：
        1、导入 Tkinter 模块
        2、创建控件
        3、指定这个控件的 master， 即这个控件属于哪一个
        4、告诉 GM(geometry manager) 有一个控件产生了。

       (1) 函数simple_display展示了一个GUI的最简单的展示。
       (2) 函数button_trigger_fun演示，在点击一个按钮时，触发一个函数。
            tkinter中，当创建新的空间时，容器要作为第一个参数传入，缺省时为主窗口。
'''
import shelve
from tkinter import *
from tkinter.messagebox import showinfo

#########################################################################################
def simple_display():
    # Widget构建器 Label ；  布局管理方法：pack ； mainloop调用启动事件处理。
    Label(text="SimpleGuiTest").pack()
    mainloop()
#########################################################################################

def reply():
    showinfo(title = 'pop' ,message ="you press the button!")

def button_trigger_fun():
    #导入 Tkinter 模块
    window = Tk()
    #创建控件,指定这个控件的 master， 即这个控件属于哪一个
    btn = Button(window,text="press",comman=reply)
    #将小部件放置到主窗口中
    btn.pack()
    #进入消息循环
    window.mainloop()

#########################################################################################

if __name__ == '__main__':
    # simple_display()
    button_trigger_fun()