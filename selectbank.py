from tkinter import*
from tkinter import messagebox
import os

lin=Tk()
lin.config(bg="aqua")
lin.geometry("500x200")

def dd():
    os.system("upiid.py")

def ll():
    os.system("creditcard.py")

def hh():
    os.system("debitcard.py")

def ii():
    os.system("ticket2.py")
    

lbl=Label(lin,bg='aqua',fg='indigo',text="Select the option",font=('arial',20,'bold'),width=40).place(x=-120,y=5)
btn=Button(lin,bg='gold',fg='black',text="Debit Card",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=hh).place(x=50,y=50)
btn=Button(lin,bg='gold',fg='black',text="Credit Card",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=ll).place(x=270,y=50)
btn=Button(lin,bg='gold',fg='black',text="UPI ID",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=dd).place(x=50,y=120)
btn=Button(lin,bg='gold',fg='black',text="Pay Later",font=('arial',10,'bold'),width=15,bd=10,relief="raised",command=ii).place(x=270,y=120)
lin.mainloop()
