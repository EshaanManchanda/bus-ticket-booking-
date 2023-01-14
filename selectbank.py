from tkinter import*
from tkinter import messagebox
import os

class selectbank:
    def __init__(self, root):
        self.lin=root
        self.lin.config(bg="aqua")
        self.lin.geometry("500x200")
        self.lbl=Label(self.lin,bg='aqua',fg='indigo',text="Select the option",font=('arial',20,'bold'),width=40).place(x=-120,y=5)
        self.btn=Button(self.lin,bg='gold',fg='black',text="Debit Card",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=self.hh).place(x=50,y=50)
        self.btn=Button(self.lin,bg='gold',fg='black',text="Credit Card",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=self.ll).place(x=270,y=50)
        self.btn=Button(self.lin,bg='gold',fg='black',text="UPI ID",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=self.dd).place(x=50,y=120)
        self.btn=Button(self.lin,bg='gold',fg='black',text="Pay Later",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=self.ii).place(x=270,y=120)

    def dd(self):
        self.lin.destroy()
        os.system("python upiid.py")

    def ll(self):
        self.lin.destroy()
        os.system("python creditcard.py")

    def hh(self):
        self.lin.destroy()
        os.system("python debitcard.py")

    def ii(self):
        self.lin.destroy()
        os.system("python Customerfirst.py")
    


if __name__ == "__main__":
    root = Tk()
    obj = selectbank(root)
    root.mainloop()

