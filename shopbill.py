from tkinter import Tk,Label,Entry,Button
from tkinter import *

def ok():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = n1 * n2
    e3.insert(0,n3)
    if(n1<11):
        e4.insert(0,"0%")
        n4 = (n3 * 0) / 100
        e5.insert(0,n4)
        n5 = n3 - n4
        e6.insert(0,n5)
    elif(n1>10 and n1<21):
        e4.insert(0,"5%")
        n4 = (n3 * 5) / 100
        e5.insert(0,n4)
        n5 = n3 - n4
        e6.insert(0,n5)
    elif(n1>20 and n1<50):
        e4.insert(0,"15%")
        n4 = (n3 * 15) / 100
        e5.insert(0,n4)
        n5 = n3 - n4
        e6.insert(0,n5)
    else:
        e4.insert(0,"25%")
        n4 = (n3 * 25) / 100
        e5.insert(0,n4)
        n5 = n3 - n4
        e6.insert(0,n5)

    
    
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)



t = Tk()     #creating object of Tk class
t.wm_title("GUI")
t.wm_geometry("600x600")
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


l = Label(master=t,text = "Quantity",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 10,width= 150,height = 30)
l = Label(master=t,text = "Price/unit",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 60,width= 150,height = 30)
l = Label(master=t,text = "Total",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 110,width= 150,height = 30)
l = Label(master=t,text = "Discount%",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 160,width= 150,height = 30)
l = Label(master=t,text = "Discount amt",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 210,width= 150,height = 30)
l = Label(master=t,text = "Payable amt",fg = 'black',font = ("Consolas",15,"bold"))
l.place(x = 50,y= 260,width= 150,height = 30)


b = Button(master=t,fg = 'red',text = "OK",font = ("Consolas",15,"bold"), command = ok)
b.place(x = 150,y = 410,width = 100,height = 30)
b1 = Button(master=t,fg = 'blue',text = "CLEAR",font = ("Consolas",15,"bold"), command = clear)
b1.place(x = 400,y = 410,width = 100,height = 30)




t.mainloop() 