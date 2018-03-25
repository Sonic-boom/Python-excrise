# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:55:24 2017

@author: akuma
"""

from tkinter import *


def hello(): print('hello')


win = Tk()
win.title('你好')
win.geometry('400x300')

btn = Button(win, text='click', command=hello)
btn.pack(expand=YES, fill=BOTH)


mainloop()
