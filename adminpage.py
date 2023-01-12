from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
from PIL import ImageTk, Image

win=Tk()
win.geometry("620x500")
win.resizable(False,False)
load=Image.open('bk.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def kk():
    num1=us.get()
    num2=pas.get()
    email="madhav@gmail.com"
    pasw="123456"
    if num1==email and num2==pasw:
        os.system("adminsecond.py")
    else:
        messagebox.showerror("Message","Check all required field")    
   
frame2=Frame(win,bd=10,relief="raised",width=600,height=350,bg="darkslategray").place(x=10,y=70)
frame3=Frame(win,bg='aquamarine',bd=9,relief="raised",width=400,height=40).place(x=96,y=130)
lb2=Label(frame3,bg='aquamarine',fg='black',text="Admin Login",font=20).place(x=240,y=134)


lb=Label(frame2,text="Username",font=('arial',12,'bold'),width=15).place(x=90,y=200)

lb2=Label(frame2,text="Password",font=('arial',12,'bold'),width=15).place(x=90,y=250)
us=StringVar()
tx=Entry(frame2,textvariable=us,font=1).place(x=270,y=200)
pas=StringVar()
tx2=Entry(frame2,textvariable=pas,font=1).place(x=270,y=250)

btn=Button(frame2,bg='aquamarine',text="LOGIN IN",font=20,bd=9,relief="raised",width=25,command=kk).place(x=170,y=300)
win.mainloop()
