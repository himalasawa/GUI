
from tkinter import Tk,Label,Entry,Button
from tkinter import *

def red():
    l.configure(fg = 'red')
def blue():
    l.configure(fg = 'blue')
def green():
    l.configure(fg = 'green')
def orange():
    l.configure(fg = 'orange')
  



t = Tk()     #creating object of Tk class
t.wm_title("GUI")
t.wm_geometry("800x400")
t.configure(bg = 'light blue')

l = Label(master=t,text = "Welcome to binary brains",fg = 'black',font = ("Consolas",15,"bold"), bg = 'yellow')
l.place(x = 100,y= 10,width= 600,height = 30)


b = Button(master=t,fg = 'red',text = "RED",font = ("Consolas",15,"bold"), command = red)
b.place(x = 150,y = 60,width = 100,height = 30)
b1 = Button(master=t,fg = 'blue',text = "BLUE",font = ("Consolas",15,"bold"), command = blue)
b1.place(x = 250,y = 60,width = 100,height = 30)
b2 = Button(master=t,fg = 'green',text = "GREEN",font = ("Consolas",15,"bold"), command = green)
b2.place(x = 350,y = 60,width = 100,height = 30)
b3 = Button(master=t,fg = 'orange',text = "ORANGE",font = ("Consolas",15,"bold"), command = orange)
b3.place(x = 450,y = 60,width = 100,height = 30)



t.mainloop()  #hold the window