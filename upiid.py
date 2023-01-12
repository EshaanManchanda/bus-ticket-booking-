from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

win=Tk()
win.config(bg="#FCE6C9")
win.geometry("620x450")
win.resizable(False,False)

frame=Frame(win,bg='red4',bd=10,relief="raised",width=400,height=50).place(x=100,y=1)
lb=Label(frame,bg='red4',fg='white',text="UPI ID",font=20).place(x=280,y=12)
frame2=Frame(win,bd=10,relief="raised",width=600,height=350,bg="red4").place(x=5,y=80)

frame3=Frame(win,bg='gold',bd=9,relief="raised",width=400,height=40).place(x=96,y=130)
lb2=Label(frame3,bg='gold',fg='black',text="UPI Details",font=18).place(x=240,y=132)

us=StringVar()
lb=Label(frame2,bg='red4',fg='gold',text="UPI ID",font=20,width=10).place(x=150,y=200)
pas=StringVar()
lb2=Label(frame2,bg='red4',fg='gold',text="Password",font=20,width=10).place(x=140,y=250)

tx=Entry(frame2,textvariable=us,font=10).place(x=250,y=200)
tx2=Entry(frame2,textvariable=pas,font=10).place(x=250,y=250)

btn=Button(frame2,bg='gold',fg='black',text="Submit",font=20,bd=9,relief="raised",width=20).place(x=190,y=320)

win.mainloop()
