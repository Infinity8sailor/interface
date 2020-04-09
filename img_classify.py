# import the necessary packages
from tkinter import *
from PIL import Image,ImageTk            #if not installed do use "pip install pillow"
import os
import shutil
import numpy


def paths(path):                #create database [data] of location of available images
    for i in  os.listdir(path):
        path1=path+"\\" +i
        if os.path.isdir(path1):
            paths(path1)
        else:
            data.append(path1)

def move(path,loc):
    if os.path.isdir(loc):
        print(loc,"exist")
        pass
    else:
        os.mkdir(loc)
    shutil.move(path,loc)
    print("file moved to ", loc)
    img0()

def delete(path):
    if os.path.exists(path):
       os.remove(path)
       print("file deleted")
       img0()
    else:
       print("The file does not exist")

    


def img0():
        global num,img, render,text
        print (num)
        num += 1
        load = Image.open(data[num])
        load=load.resize((480,480), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img.config(image=render)
        text.config(text=str(num))


if __name__ == "__main__" :
    root=Tk()
    path0="V:\home"                  #source of images
    data=[] 
    num=0
    paths(path0)                     #database creating
    data = [ file for file in data if  file.endswith( ('.jpg','.png') ) ]
    load = Image.open(data[num]).resize((480,480), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img=Label(root,image=render)
    img.pack(side=LEFT)
    text=Label(root,text=str(num))
    text.pack(side=TOP)
    Button(root, text="delete", command= lambda : delete(data[num])).pack(side =RIGHT)       #CAUTION using this button (here lambda is very imp if removed you will lose all photos with location saved in data)
    Button(root, text="next", command= lambda : img0()).pack(side =RIGHT)
    Button(root, text="trek", command= lambda : move(data[num],path0+"\\images\\trek")).pack(side =RIGHT)        #buttons for location whrer you want to keep photos
    Button(root, text="family", command= lambda : move(data[num],path0+"\\images\\family")).pack()
    Button(root, text="other", command= lambda : move(data[num],path0+"\\images\\other")).pack()
    Button(root, text="hostel", command= lambda : move(data[num],path0+"\\images\\hostel")).pack()
    Button(root, text="college", command= lambda : move(data[num],path0+"\\images\\college")).pack()
    Button(root, text="jawla bazar", command= lambda : move(data[num],path0+"\\images\\jawla_bazar")).pack()

    root.mainloop()
