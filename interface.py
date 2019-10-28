print('Interface is started ..........\nlets get started')
from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter as tk
import sys
import time
import json
from multiprocessing import Process
#import urllib.request
#from subprocess import Popen, PIPE, STDOUT

gtime=time.time()
root=Tk()
root.configure(background='black')
root.option_add( "*font", "lucida 12 bold italic" )
#Scrollbar(root).grid( row=200,column=200)
with open("C:/Users/vaibhav/interface_data.json") as f:
            data=json.load(f)
            f.close 


class creator:
    def win_float():
        def f_add_project(project_name,completion,dead_line):
            data["projects"][project_name]=[completion,dead_line]
            dump_data(data)
            float_root.destroy()
            creator.clear()
    
        def f_delete_project(project):
           del data["projects"][project]
           dump_data(data)
           float_root.destroy()
           creator.clear()
        
        def f_add_track(project,deadline):
            data["tracks"][project]=[deadline]
            dump_data(data)
            float_root.destroy()
            creator.clear()         
        
    
        def f_del_track(project):
            del data["tracks"][project]
            dump_data(data)
            float_root.destroy()
            creator.clear()
            
        def f_week_update(day,hours,state):
            data["days"][day][int(hours)]=state
            dump_data(data)
            float_root.destroy()
            creator.clear()
                
        float_root=Tk()
        float_root.configure(background='black')
        float_root.option_add( "*font", "lucida 12 bold italic" )
        tk.Label(float_root,bg="black",fg="green",text="project_name").grid(row=0,column=0)
        tk.Label(float_root,bg="black",fg="green",text="completion_status").grid(row=0,column=2)
        tk.Label(float_root,bg="black",fg="green",text="dead_line").grid(row=0,column=4)
        tk.Label(float_root,bg="black",fg="green",text="delete_project").grid(row=1,column=0)
        tk.Label(float_root,bg="black",fg="green",text="track").grid(row=2,column=0)
        tk.Label(float_root,bg="black",fg="green",text="day/hour/status").grid(row=3,column=0)
        tk.Label(float_root,bg="black",fg="green",text="status >> empty=0,extra=1,college=2").grid(row=3,column=4)
        
        add_project   =tk.Entry(float_root)
        add_completion=tk.Entry(float_root)
        add_deadline  =tk.Entry(float_root)
        delete_project=tk.Entry(float_root)
        add_track     =tk.Entry(float_root)
        add_day       =tk.Entry(float_root)
        add_hour      =tk.Entry(float_root)
        add_status    =tk.Entry(float_root)
        
        add_project.grid(row=0,column=1)
        add_completion.grid(row=0,column=3)
        add_deadline.grid(row=0,column=5)
        delete_project.grid(row=1,column=1)
        add_track.grid(row=2,column=1)
        add_day.grid(row=3,column=1)
        add_hour.grid(row=3,column=2)
        add_status.grid(row=3,column=3)
        
        tk.Button(float_root,text='add_project',bg="black",fg="green",command=lambda : f_add_project(add_project.get(),int(add_completion.get()),add_deadline.get())).grid(row=5,column=0)
        tk.Button(float_root,text='delete_project',bg="black",fg="green",command=lambda : f_delete_project(delete_project.get())).grid(row=5,column=1)
        tk.Button(float_root,text='add_track',bg="black",fg="green",command=lambda : f_add_track(add_track.get(),add_deadline.get())).grid(row=5,column=2)
        tk.Button(float_root,text='del_track',bg="black",fg="green",command=lambda : f_del_track(add_track.get())).grid(row=5,column=3)
        tk.Button(float_root,text='week_data',bg="black",fg="green",command=lambda : f_week_update(add_day.get(),add_hour.get(),add_status.get())).grid(row=5,column=4)
        float_root.mainloop()
    
    def clear():
        i=1
        print(i-1)
        for widget in root.winfo_children():
            widget.destroy()
            i+=1
        root_data(root)
    
    def day_task_update():
        pass
        
    
        
def load_data():
        with open("C:/Users/vaibhav/interface_data.json") as f:
            data=json.load(f)
            f.close 
def dump_data(edited_data):
        with open("C:/Users/vaibhav/interface_data.json","w") as f:
            json.dump(edited_data,f)
            f.close

def close(one):
        global gtime
        ctime=gtime
        while gtime < (ctime+(20)):
               print(gtime)
               gtime=time.time()
               pass
        print("one")    
        one.quit()
        
class refresh():
    def refresh_data():
        root.update()
        load_data()
        j=0
        for i in (data["projects"]).keys():
            def progress_bar(n,m):
              for i in range(n+1): 
               c=int(i*2.5)
               color_code=("i"+"m")
               color='#%02x%02x%02x' % (255-c,c, 0)
               s = ttk.Style()
               s.theme_use('clam')
               
               s.configure((color_code+".Horizontal.TProgressbar"), background=color ,foreground="red")
               progress["style"]=color_code+".Horizontal.TProgressbar"
               progress['value'] = i
               completion["text"]=str(i)+"%"   #data["projects"][i]
               root.update()
               time.sleep(.021)
               
            tk.Label(project_frame,text=j+1,bg="black",fg="green",).grid(row=j+1,column=0)
            tk.Label(project_frame,text=i,bg="black",fg="green",).grid(row=j+1,column =1)
            progress=Progressbar(project_frame, orient = HORIZONTAL,length = 400, mode = 'determinate' ,max=100 )
            completion=Label(project_frame,text="0%")
            progress.grid(row=j+1,column=2)
            completion.grid(row=j+1,column=2)
            progress_bar(data["projects"][i][0],i)
            tk.Label(project_frame,text=data["projects"][i][1],bg="black",fg="green",).grid(row=j+1,column =3)
            #tk.Button(root,text="delete",command=lambda: refresh.delete_project(data["projects"][i])).grid(row=j+1,column =3)
            j+=1
        j=0   
        for i in data["tracks"].keys():
            tk.Label(tracks_frame,text=j+1,bg="black",fg="green",).grid(row=j+1,column=0)
            tk.Label(tracks_frame,text=i,bg="black",fg="green",).grid(row=j+1,column =1)
            j+=1       
        
        j=0
        
        for i in data["days"].keys():
            def progress_color(i,n,r,c):
                color=data["days"][i][n]
                if color=="1"or color==1:
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure("green.Horizontal.TProgressbar", background='green')
                    Progressbar(week_frame, style="green.Horizontal.TProgressbar", orient="horizontal", length=20, mode="determinate", maximum=2, value=2).grid(row=r, column=c)
                else:
                    pass
                
                if color=="2"or color==2:
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure("blue.Horizontal.TProgressbar", background='blue')
                    Progressbar(week_frame, style="blue.Horizontal.TProgressbar", orient="horizontal", length=20, mode="determinate", maximum=2, value=2).grid(row=r, column=c)
                else :
                    pass
                
                if color=="0" or color==0:
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure("red.Horizontal.TProgressbar", background='red')
                    Progressbar(week_frame, style="red.Horizontal.TProgressbar", orient="horizontal", length=20, mode="determinate", maximum=2, value=2).grid(row=r, column=c)
                else :
                    pass
            tk.Label(week_frame,text=j+1,bg="black",fg="green",).grid(row=j+1,column=0)
            tk.Label(week_frame,text=i,bg="black",fg="green",).grid(row=j+1,column =1)
           
            for n in range(23):
                tk.Label(week_frame,text=n,bg="black",fg="red",).grid(row=0,column=n+2)
                progress_color(i,n,j+1,2+n)
            tk.Button(week_frame,text="+" ,bg="black",fg="green",command=lambda: creator.win_float()).grid( row=j+1,column =26)
            root.update()
            j+=1       
        j=0
        def add_window():
                def add_task(a,b,c,d):
                    data["today"][a]=[int(b),int(c),int(d)]
                    dump_data(data)
                    add_window_float.destroy()
                    creator.clear()
                    
                add_window_float=Tk()
                add_window_float.configure(background='black')
                add_window_float.option_add( "*font", "lucida 12 bold italic" )
                tk.Label(add_window_float,bg="black",fg="red",text="task").grid(row=0,column=0)
                tk.Label(add_window_float,bg="black",fg="red",text="From").grid(row=0,column=2)
                tk.Label(add_window_float,bg="black",fg="red",text="To").grid(row=0,column=4)
        
                task=tk.Entry(add_window_float)
                From=tk.Entry(add_window_float)
                To=tk.Entry(add_window_float)
                
                task.grid(row=0,column=1)
                From.grid(row=0,column=3)
                To.grid(row=0,column=5)
                
                tk.Button(add_window_float,text="add",command=lambda:add_task(task.get(),From.get(),To.get(),0),bg="black",fg="green",).grid(row=1,column=0)
                
                
                add_window_float.mainloop()
            
                
        def day_task_update(i):
                t=0
                print("yes")
                if data["today"][i][2]==0:
                    data["today"][i][2]=1
                else:
                    data["today"][i][2]=1
                n=len(data["today"])
                for a in data["today"].keys():
                    if data["today"][a][2]==1:
                        t+=1
                    else:
                        pass
                percent=int((t/n)*100)   
                progress1['value'] =percent
                completion1["text"]=str(percent)+"%"   #data["projects"][i]
                root.update()
                data["today"]["lets start"][2]=0
                dump_data(data)
                load_data()
                        #time.sleep(.021)       
                        
        def clear_task():
            data["today"]={"lets start":[0,0,0]}
            dump_data(data)
            
        
                        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("green.Horizontal.TProgressbar", background='green')
        progress1=Progressbar(today_frame,style="green.Horizontal.TProgressbar", orient = HORIZONTAL,length = 400, mode = 'determinate' ,max=100 )
        completion1=Label(today_frame,text="0%")
        progress1.grid(row=1,column=1)
        completion1.grid(row=1,column=1)
        day_task_update("lets start")                
        for i in data["today"].keys():
            tk.Label(today_frame, text=j+1,bg="black",fg="blue").grid(row=j+2,column=0)
            tk.Label(today_frame, text=i,bg="black",fg="blue").grid(row=j+2,column=1)
            tk.Button(today_frame,text="!",bg="black",fg="yellow",command=lambda:day_task_update(i) ).grid(row=j+2,column=3)
            tk.Button(today_frame,text="add",bg="black",fg="green",command=lambda:add_window() ).grid(row=0,column=0)
            tk.Button(today_frame,text="clear",bg="black",fg="green",command=lambda:clear_task() ).grid(row=0,column=2)
            Checkbutton(today_frame, text="done").grid(row=j+2,column=4)
            
            j+=1
            
        
    
class root_data():
    
    def __init__(self,root):
        self.root=root
        root.geometry('720x480+400+400')
        
        global project_frame
        global week_frame
        global tracks_frame
        global today_frame
        
        project_frame=tk.Frame(root,bg="black",width=250, height=190,highlightbackground="green", highlightcolor="orange", highlightthickness=11, bd=2)
        week_frame=tk.Frame(root,bg="black",highlightbackground="red", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 5)
        tracks_frame=tk.Frame(root,bg="black",highlightbackground="blue", highlightcolor="green", highlightthickness=4, width=100, height=100, bd= 11)
        today_frame=tk.Frame(root,bg="black",highlightbackground="orange", highlightcolor="green", highlightthickness=7, width=100, height=100, bd= 15)
        
        project_frame.grid(row=1,column=0)
        week_frame.grid(row=2,column=0)
        tracks_frame.grid(row=1,column=1)
        today_frame.grid(row=2,column=1)

        root.title("The interface")
        localtime = time.asctime( time.localtime(time.time()) )
        button0=tk.Button(root,text='exit',command=exit,bg="black",fg="red")
        menubar=Menu(root,)

        GO=Menu(menubar,bg="green",tearoff=0,activebackground='red')
        online=Menu(menubar,tearoff=0)
        personal=Menu(menubar,tearoff=0)
    
        menubar.add_cascade(label='GO',menu=GO)
        menubar.add_cascade(label='online',menu=online)
        menubar.add_cascade(label='personal',menu=personal)
        menubar.add_cascade(label=localtime)

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
    
        button0.grid(row=0,column=5)
        root.config(menu=menubar)
        button=tk.Button(root,text="add project",bg="black",fg="green",command=creator.win_float)
        button1=tk.Button(root,text="refresh",bg="black",fg="green",command=lambda: creator.clear())
        label1=tk.Label(project_frame,text="Ongoing projects",bg="black",fg="green",)
        label2=tk.Label(project_frame,text="Deadline",bg="black",fg="red",)
        label3=tk.Label(week_frame,text="week time",bg="black",fg="green",)
        label4=tk.Label(today_frame,text="today",bg="black",fg="green",)
        button2=tk.Button(root,text="delete_project",bg="black",fg="red",command=creator.win_float)
        button.grid(row=0,column=0)
        button1.grid(row=0,column=1)
        label1.grid(row=0,column=2)
        label2.grid(row=0,column=3)
        label3.grid(row=0,column=1)
        label4.grid(row=0,column=1)
        
        button2.grid(row=0,column=4)
        label=tk.Label(tracks_frame,text="daily track-ups",bg="black",fg="green",).grid(row=0,column=1)
        button3=tk.Button(root,text="add_tracks",bg="black",fg="green",command=creator.win_float).grid(row=0,column=8)
        
        
        
        
        
        refresh.refresh_data()
        root.mainloop()
        
root_data(root)        
'''             
if __name__ == '__main__':
    
    Process(target=close(root),root_data(root)).start()
    #Process(target=root_data(root)).start()
'''


