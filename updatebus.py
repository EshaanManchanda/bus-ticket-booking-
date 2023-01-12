from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

win=Tk()
win.config(bg="teal")
win.geometry("400x300")
win.resizable(False,False)

us=StringVar()
lb=Label(bg='Teal',fg='white',text="Old Route Number",font=('arial',12,'bold'),width=20).place(x=0,y=70)

lb=Label(bg='Teal',fg='white',text="New Route Number",font=('arial',12,'bold'),width=20).place(x=0,y=100)
tx=Entry(textvariable=us).place(x=200,y=70,width=150)
tx=Entry(textvariable=us).place(x=200,y=100,width=150)
btn=Button(bg='aquamarine',fg='black',text="Search",font=20,bd=9,relief="raised",width=15).place(x=100,y=150)
win.mainloop()
