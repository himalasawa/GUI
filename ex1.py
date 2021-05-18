from tkinter import Tk,Label,Entry,Button
from tkinter import *

def show():
    e.insert(0,"Binary Brains")



t = Tk()     #creating object of Tk class
t.wm_title("GUI")
t.wm_geometry("800x400")
t.configure(bg = 'light blue')

l = Label(master=t,text = "Enter Name:",fg = 'blue',font = ("Consolas",15,"bold"))
l.place(x = 10,y= 10,width= 190,height = 30)

e = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e.place(x = 220,y= 10,width= 300,height = 30)

b = Button(master=t,fg = 'purple',text = "Click me",font = ("Consolas",15,"bold"), command = show)
b.place(x = 50,y = 60,width = 100,height = 30)



t.mainloop()  #hold the window