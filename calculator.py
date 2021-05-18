from tkinter import *

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = n1 + n2
    e3.insert(0,n3)
def sub():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = n1 - n2
    e3.insert(0,n3)
def mul():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = n1 * n2
    e3.insert(0,n3)    
def div():
    n1 = int(e1.get())
    n2 = int(e2.get())
    n3 = n1 / n2
    e3.insert(0,n3)

t = Tk()     #creating object of Tk class
t.wm_title("GUI")
t.wm_geometry("800x400")
t.configure(bg = 'light blue')

e1 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e1.place(x = 20,y= 20,width= 190,height = 30)

e2 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e2.place(x = 240,y= 20,width= 190,height = 30)

e3 = Entry(master=t,fg = 'red',font = ("Consolas",15,"bold"))
e3.place(x = 460,y= 20,width= 190,height = 30)

btnadd = Button(master=t,fg = 'purple',text = "Add",font = ("Consolas",15,"bold"),command = add)
btnadd.place(x = 20,y = 60,width = 100,height = 30)
btnsub = Button(master=t,fg = 'purple',text = "Sub",font = ("Consolas",15,"bold"),command = sub)
btnsub.place(x = 20,y = 90,width = 100,height = 30)
btnmul = Button(master=t,fg = 'purple',text = "Mul",font = ("Consolas",15,"bold"),command = mul)
btnmul.place(x = 20,y = 120,width = 100,height = 30)
btndiv = Button(master=t,fg = 'purple',text = "Div",font = ("Consolas",15,"bold"),command = div)
btndiv.place(x = 20,y = 150,width = 100,height = 30)



t.mainloop()