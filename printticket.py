from tkinter import*
import os

root=Tk()
root.geometry("800x750")
root.title("Welcome To Bus Portal")
root.config(bg="Teal")
root.resizable(False,False)


fr=Frame(root,width=800,bd=10,height=50,relief="raised")
fr.place(x=0,y=5)
frlb=Label(fr,text="Ticket",font=('arial',15,'bold'),width=15)
frlb.place(x=270,y=0)
    
lb=Label(root,text="Bus Route",font=('arial',15,'bold'),width=20).place(x=19,y=100)
fro=StringVar()
tx=Entry(root,font=10,textvariable=fro)
tx.place(x=300,y=100)
too=StringVar()
tx2=Entry(root,font=10,textvariable=too)
tx2.place(x=550,y=100)
    
typ=StringVar()
        
lb2=Label(root,text="Bus Type",font=('arial',15,'bold'),width=20).place(x=19,y=150)
tx2=Entry(root,font=10,textvariable=typ).place(x=300,y=150)
    
rn=StringVar()
        
lb3=Label(root,text="Route Number",font=('arial',15,'bold'),width=20).place(x=19,y=200)
tx =Entry(root,font=10,textvariable=rn).place(x=300,y=200)
    
fare=StringVar()
lb4=Label(root,text="Per Seat Fare",font=('arial',15,'bold'),width=20).place(x=19,y=250)
text1=Label(root,text="",font=('arial',15,'bold'),textvariable=fare).place(x=300,y=250)
    
nop=StringVar()
lb5=Label(root,text="Number of Passenger",font=('arial',15,'bold'),width=20).place(x=19,y=300)
text2=Label(root,text="",font=('arial',15,'bold'),textvariable=nop).place(x=300,y=300)
    
tsf=StringVar()
lb6=Label(root,text="Total Seat Fare",font=('arial',15,'bold'),width=20).place(x=19,y=350)
tx7=Entry(root,font=10,textvariable=tsf).place(x=300,y=350)
    
mc=StringVar()
lb7=Label(root,text="Meal Cost",font=('arial',15,'bold'),width=20).place(x=19,y=400)
tx8=Entry(root,font=10,textvariable=mc).place(x=300,y=400)
    
tf=StringVar()
lb8=Label(root,text="Total Fare",font=('arial',15,'bold'),width=20).place(x=19,y=450)
tx9=Entry(root,font=10,textvariable=tf).place(x=300,y=450)
    
tax=StringVar()
lb9=Label(root,text="Tax",font=('arial',15,'bold'),width=20).place(x=19,y=500)
tx10=Entry(root,font=10,textvariable=tax).place(x=300,y=500)
    
tpf=StringVar()
lb10=Label(root,text="Total Paybel For",font=('arial',15,'bold'),width=20).place(x=19,y=550)
tx10=Entry(root,font=10,textvariable=tpf).place(x=300,y=550)
btn=Button(root,text="Print Ticket",font=('arial',10,'bold'),width=12,bd=8,relief="raised").place(x=250,y=650)

mainloop()
