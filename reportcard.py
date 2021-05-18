from tkinter import Tk,Label,Entry,Button
from tkinter import *

def ok():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = int(e3.get())
    n4 = int(e4.get())
    n5 = int(e5.get())
    n6 = n1 + n2 + n3 + n4 +n5
    n7 = n6 / 5
    e6.insert(0,n6)
    e7.insert(0,n7)
    
def close():
    t.destroy()

  



t = Tk()     #creating object of Tk class
t.wm_title("GUI")
t.wm_geometry("800x600")
t.configure(bg = 'light blue')
e1 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e1.place(x = 400,y= 10,width= 100,height = 30)

e2 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e2.place(x = 400,y= 60,width= 100,height = 30)

e3 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e3.place(x = 400,y= 110,width= 100,height = 30)

e4 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e4.place(x = 400,y= 160,width= 100,height = 30)

e5 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e5.place(x = 400,y= 210,width= 100,height = 30)

e6 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e6.place(x = 400,y= 260,width= 100,height = 30)
e7 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e7.place(x = 400,y= 310,width= 100,height = 30)

l = Label(master=t,text = "math",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 10,width= 60,height = 30)
l = Label(master=t,text = "chem",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 60,width= 60,height = 30)
l = Label(master=t,text = "phy",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 110,width= 60,height = 30)
l = Label(master=t,text = "hindi",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 160,width= 60,height = 30)
l = Label(master=t,text = "eng",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 210,width= 60,height = 30)
l = Label(master=t,text = "total",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 260,width= 60,height = 30)
l = Label(master=t,text = "per",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 310,width= 60,height = 30)

b = Button(master=t,fg = 'red',text = "OK",font = ("Consolas",15,"bold"), command = ok)
b.place(x = 150,y = 410,width = 100,height = 30)
b1 = Button(master=t,fg = 'blue',text = "CLOSE",font = ("Consolas",15,"bold"), command = close)
b1.place(x = 400,y = 410,width = 100,height = 30)




t.mainloop() 