import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

import tkinter.ttk as ttk

root=Tk()


s = ttk.Style()
s.theme_use('clam')
def progress_bar(n):
    for i in range(n):
        c=int(i*2.5)
        color='#%02x%02x%02x' % (255-c,c, 30)
        s.configure("green.Horizontal.TProgressbar", background=color)
        progress['value'] = i
        root.update()
        time.sleep(.131)









'''
def progress_bar(n):
    for i in range(n):
        if i<80:
            if i <60:
                if i<30:
                    if i<10:
                        s.configure("green.Horizontal.TProgressbar", background='red')
                        progress['value'] = i
                        root.update()
                        time.sleep(.031)
                    else:
                        pass
                else:
                    s.configure("green.Horizontal.TProgressbar", background='yellow')
                    progress['value'] = i
                    root.update()
                    time.sleep(.031)
            else:
                s.configure("green.Horizontal.TProgressbar", background='green')
                progress['value'] = i
                root.update()
                time.sleep(.031)   
                    
        else:
            s.configure("green.Horizontal.TProgressbar", background='green')
            progress['value'] = i
            root.update()
            time.sleep(.011)  
'''                    
'''
def progress_bar(n):
        for i in range(n+1): 
            if i < 20:   
               s.configure("green.Horizontal.TProgressbar", background='red')
               progress['value'] = i
               root.update()
               time.sleep(.011)
            if i < 40:   
               s.configure("green.Horizontal.TProgressbar", background='yellow')
               progress['value'] = i
               root.update()
               time.sleep(.011)
            if i < 60:   
               s.configure("green.Horizontal.TProgressbar", background='orange')
               progress['value'] = i
               root.update()
               time.sleep(.011)   
            if i < 80:   
               s.configure("green.Horizontal.TProgressbar", background='blue')
               progress['value'] = i
               root.update()
               time.sleep(.011)   
            if i < 101:   
               s.configure("green.Horizontal.TProgressbar", background='red')
               progress['value'] = i
               root.update()
               time.sleep(.011)   
               
'''               
progress=Progressbar(root,style="green.Horizontal.TProgressbar", orient = HORIZONTAL,length = 400, mode = 'determinate' ,max=100)

progress.pack()
progress_bar(100)
root.mainloop()