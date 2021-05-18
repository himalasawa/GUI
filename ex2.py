from tkinter import Tk,Label,Entry,Button
from tkinter import *

def show():
    pass
    
    
def copy():
    s = e.get()
    e1.insert(0,s)
def clear():
    e.delete(0,END)
    e1.delete(0,END)
t = Tk()     
t.wm_title("GUI")
t.wm_geometry("800x400")
t.configure(bg = 'light blue')
e = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e.place(x = 20,y= 10,width=200 ,height = 30)
e1 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e1.place(x = 400,y= 10,width= 200,height = 30)
b = Button(master=t,fg = 'purple',text = "copy",font = ("Consolas",15,"bold"), command = copy)
b.place(x = 20,y = 60,width = 100,height = 30)
b1 = Button(master=t,fg = 'purple',text = "Clear",font = ("Consolas",15,"bold"), command = clear)
b1.place(x = 400,y = 60,width = 100,height = 30)
t.mainloop()  