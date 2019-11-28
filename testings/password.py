import tkinter as tk
from tkinter import *

def login():
    if user.get()=='cosmic'and pass_word.get()=="94210844":
        root=Tk()
        pre_root.destroy()
        root.mainloop()
        
    else:
        print("wrong password")
        
pre_root=Tk()
tk.Label(pre_root, text = "Username").grid(row = 0)
user=tk.Entry(pre_root)
user.grid(row=0,column=1)

tk.Label(pre_root,text="password").grid(row=1)
pass_word=tk.Entry(pre_root)
pass_word.grid(row=1,column=1)
tk.Checkbutton(pre_root, text = "Keep Me Logged In").grid(columnspan = 2)
tk.Button(pre_root,text='inter_now',command=lambda  : login()).grid(row=3)



pre_root.mainloop()

