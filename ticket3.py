from tkinter import*
from PIL import Image, ImageTk
import os 

lin=Tk()
lin.geometry("700x500")
lin.title("Welcome To Bus Portal")
lin.config(bg="grey")
lin.resizable(False,False)
load=Image.open('bk.jpg')
render=ImageTk.PhotoImage(load)
img=Label(lin,image=render)
img.place(x=0,y=0)
fr=Frame(lin,width=700,bd=10,height=50,relief="raised").place(x=0,y=5)
frlb=Label(fr,text="Ticket",font=('arial',15,'bold'),width=20).place(x=220,y=12)

lb=Label(lin,text="Name",font=('arial',15,'bold'),width=20).place(x=19,y=100)
tx=Entry(lin,font=10).place(x=300,y=100)
lb2=Label(lin,text="Phone Number",font=('arial',15,'bold'),width=20).place(x=19,y=150)
tx2=Entry(lin,font=10).place(x=300,y=150)
lb3=Label(lin,text="Email",font=('arial',15,'bold'),width=20).place(x=19,y=200)
tx=Entry(lin,font=10).place(x=300,y=200)
lb4=Label(lin,text="Number of Passenger",font=('arial',15,'bold'),width=20).place(x=19,y=250)
tx=Entry(lin,font=10).place(x=300,y=250)
lb5=Label(lin,text="Fare",font=('arial',15,'bold'),width=20).place(x=19,y=300)
tx=Entry(lin,font=10).place(x=300,y=300)

def ope():
    os.system("selectbank.py")
    
#Buttons
btn=Button(lin,text="Pay",command=ope,font=('arial',10,'bold'),width=12,bd=8,relief="raised").place(x=250,y=400)

lin.mainloop()
