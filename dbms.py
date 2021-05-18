from tkinter import *
from pymysql import *

class CustomerGUI:
    
    def _init_(self):
        self.root = Tk()
        self.root.geometry("600x600")

        self.lblcustid = Label(self.root, text="Custid:",font=("Times", 15, "bold"))
        self.lblcustid.place(x = 30,y=20,width = 70,height = 30)
        self.encustid = Entry(self.root, font=("Times", 15, "bold"))
        self.encustid.place(x = 120,y=20,width = 300,height = 30)

        self.lblname = Label(self.root, text="Name:",font=("Times", 15, "bold"))
        self.lblname.place(x = 30,y=70,width = 70,height = 30)
        self.enname = Entry(self.root, font=("Times", 15, "bold"))
        self.enname.place(x = 120,y=70,width = 300,height = 30)

        self.lbladdress = Label(self.root, text="Address:",font=("Times", 15, "bold"))
        self.lbladdress.place(x = 30,y=120,width = 70,height = 30)
        self.enaddress = Entry(self.root, font=("Times", 15, "bold"))
        self.enaddress.place(x = 120,y=120,width = 300,height = 200)

        self.lbldate = Label(self.root, text="Date:",font=("Times", 15, "bold"))
        self.lbldate.place(x = 30,y=340,width = 70,height = 30)
        self.endate = Entry(self.root, font=("Times", 15, "bold"))
        self.endate.place(x = 120,y=340,width = 300,height = 30)

        
        self.lblmobile = Label(self.root, text="Mobile:",font=("Times", 15, "bold"))
        self.lblmobile.place(x = 30,y=390,width = 70,height = 30)
        self.enmobile = Entry(self.root, font=("Times", 15, "bold"))
        self.enmobile.place(x = 120,y=390,width = 300,height = 30)

        self.root.mainloop()






def main():
    obj = CustomerGUI()


main() 