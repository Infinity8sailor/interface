print('lets get started')
from tkinter import *
import tkinter as tk
import sys
import time
import urllib.request
from subprocess import Popen, PIPE, STDOUT
proj_num=0

class creator:
    def __init__(self):
        self.rootf=Tk()
        self.add_entry=tk.Entry(self.rootf)
        self.add_entry.grid(row=0,column=0)
        tk.Button(self.rootf,text='add_project',command=lambda : creator.add_project("cool")).grid(row=1,column=0)
        self.rootf.mainloop()
    
    def add_project(project_name):
        global proj_num
        tk.Label(call.master,text=proj_num+1).grid(row=proj_num+1,column=0)
        tk.Label(call.master,text=project_name).grid(row=proj_num+1,column =1)
        proj_num+=1
        
class root_data():
    def __init__(self,master):
        self.master=master
        self.frame=Frame(master)
        self.frame.pack()
        
    def start(self):
        button_ex=tk.Button(self.frame,text='exit',command=exit)
        menubar=Menu(master)

        GO=Menu(menubar,bg="green",tearoff=0,activebackground='red')
        online=Menu(menubar,tearoff=0)
        personal=Menu(menubar,tearoff=0)
    
        menubar.add_cascade(label='GO',menu=GO)
        menubar.add_cascade(label='online',menu=online)
        menubar.add_cascade(label='personal',menu=personal)

        GO.add_command(label='live',command=exit)
        GO.add_command(label='upcoming projects',command=exit)
        GO.add_command(label='vit',command=exit)
        GO.add_command(label='infinity',command=exit)
        GO.add_command(label="social",command=exit)
        online.add_command(label='insta',command=exit)
        online.add_command(label='website',command=exit)
        online.add_command(label='v-iot',command=exit)
        online.add_command(label='vit-database',command=exit)
        online.add_command(label="google",command=lambda: url('http://google.com'))
        personal.add_command(label='attitude',command=exit)
        personal.add_command(label='life goals',command=exit)
        personal.add_command(label='resume',command=exit)
        personal.add_command(label='GP',command=exit)
        personal.add_command(label="sop",command=exit)
    
        master.config(menu=menubar)
        button=tk.Button(self.frame,text="add project",command=lambda : creator())
        button.grid(row=0,column=0)
        button_ex.grid()

      
        



        
        
        
def url(web):
    with urllib.request.urlopen(web) as response:
     html = response.read()
    test=Text(root)
    test.insert(INSERT,html)
    test.pack()
   
def ping_test():
    cmd = 'ping www.google.com'
    p = Popen(cmd.split(), stdout=PIPE, stderr=STDOUT)
    for line in iter(p.stdout.readline,''):
        ping = tk.Label(root, text=line)
        ping.pack()
  

class login_page:
    
    def __init__(self,master):
        self.frame=Frame(master)
        tk.Label(self.frame, text = "Username").grid(row = 0)
        self.user=tk.Entry(self.frame)
        self.user.grid(row=0,column=1)
        print("loop")
    
        tk.Label(self.frame,text="password").grid(row=1)
        self.pass_word=tk.Entry(self.frame)
        self.pass_word.grid(row=1,column=1)
        self.v1=IntVar()
        tk.Checkbutton(self.frame, text = "Keep Me Logged In", variable=self.v1).grid(columnspan = 2)
        tk.Button(self.frame,text='inter_now',command=lambda: login_page).grid(row=3)
        self.frame.pack()
        
    def pre_login():
        print("good")
        if (log.user.get()=='cosmic'and log.pass_word.get()=="94210844")or(log.v1.get()==1):
            print("pass")
            call.start   
            log.frame.destroy()
           
        else:
            print('error')  
            log.frame.destroy()
            log
          
root=Tk()
root.geometry('550x700+400+400')
root.title("The interface")
log=login_page(root)
call =root_data(root)
root.mainloop()





