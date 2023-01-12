from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

win=Tk()
win.config(bg="#E3CF57")
win.geometry("628x450")
win.resizable(False,False)

frame=Frame(win,bg='white',bd=10,relief="raised",width=400,height=50).place(x=100,y=1)
lb=Label(frame,bg='white',fg='blue',text="Credit Card",font=20).place(x=250,y=10)
frame2=Frame(win,bd=10,relief="raised",width=600,height=350,bg="dark blue").place(x=10,y=70)

frame3=Frame(win,bg='white',bd=9,relief="raised",width=400,height=40).place(x=96,y=130)
lb2=Label(frame3,bg='white',fg='blue',text="Card Details",font=20).place(x=250,y=133)

us=StringVar()
lb=Label(frame2,bg='aqua',fg='indigo',text="Card Number",font=20,width=12).place(x=130,y=200)
pas=StringVar()
lb2=Label(frame2,bg='aqua',fg='indigo',text="Pin",font=20,width=12).place(x=130,y=250)
                                                                           
tx=Entry(frame2,textvariable=us,font=5).place(x=300,y=200)
tx2=Entry(frame2,textvariable=pas,font=5).place(x=300,y=250)

btn=Button(frame2,bg='white',fg='blue',text="Submit",font=20,bd=9,relief="raised",width=20).place(x=190,y=300)
mainloop()
