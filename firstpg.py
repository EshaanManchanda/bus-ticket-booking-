from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

win=Tk()
win.config(bg="teal")
win.geometry("620x500")
win.resizable(False,False)

def ad():
    os.system("adminpage.py")

def cust():
    os.system("Customerfirst.py")
   
frame2=Frame(win,bd=10,relief="raised",width=600,height=350,bg="grey").place(x=10,y=70)
frame3=Frame(win,bg='aquamarine',bd=9,relief="raised",width=500,height=40).place(x=60,y=100)
lb2=Label(frame3,bg='aquamarine',fg='black',text="E-BUS TICKETING SYSTEM",font=20).place(x=200,y=103)

btn=Button(frame2,bg='lightblue3',text="ADMIN",command=ad,font=20,bd=9,relief="raised",width=20).place(x=200,y=200)
btn=Button(frame2,bg='lightblue3',text="CUSTOMER",command=cust,font=20,bd=9,relief="raised",width=20).place(x=200,y=300)
                
win.mainloop()
