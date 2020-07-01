import tkinter
import depcal
import vamail
import test
import semail
import graph
import graph2
import os
import threading
import movie
class rws():
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
    def run(self):
        
        os.system('emotionspeach.pyc')
        
       
class rs():
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
    def run(self):
        
        rws()
        
        os.system('test.pyc')
        

class r():
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
    def run(self):
        rs()
        
        os.system('workvidetest.pyc')
        
    
tr=r()
top = tkinter.Tk()
top.geometry('430x400')
def test():
    depcal.test()

def mail():
    vamail.sem()

def graph0():
    graph2.re()
def moviek():
    movie.m()

  
w=tkinter.Button(top,text='test ur depression',font='time 14',command=lambda:test())
w.place(x=0,y=0)

w2=tkinter.Button(top,text='send report ',font='time 14',command=lambda:mail())
w2.place(y=40)
w3=tkinter.Button(top,text='see graph',font='time 14',command=lambda:graph0())
w3.place(y=80)
w3=tkinter.Button(top,text='movie recommendation',font='time 14',command=lambda:moviek())
w3.place(y=120)
# Code to add widgets will go here...
top.mainloop()

