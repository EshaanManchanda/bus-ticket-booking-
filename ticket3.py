from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import os 
import sqlite3

class payment:
    def __init__(self, root):
        self.lin=root
        self.lin.geometry("700x500")
        self.lin.title("Welcome To Bus payment")
        self.lin.config(bg="grey")
        self.lin.resizable(False,False)
        self.load=Image.open('bk.jpg')

        self.render=ImageTk.PhotoImage(self.load)
        self.img=Label(self.lin,image=self.render)
        self.img.place(x=0,y=0)
        self.fetch_data()

        self.fr=Frame(self.lin,width=700,bd=10,height=50,relief="raised").place(x=0,y=5)
        self.frlb=Label(self.fr,text="Ticket",font=('arial',15,'bold'),width=20).place(x=220,y=12)

        self.lb=Label(self.lin,text="Name",font=('arial',15,'bold'),width=20).place(x=19,y=100)
        self.tx=Label(self.lin,font=10,text=self.name,width=25)
        self.tx.place(x=300,y=100)

        self.lb2=Label(self.lin,text="Phone Number",font=('arial',15,'bold'),width=20).place(x=19,y=150)
        self.tx2=Label(self.lin,font=10,text=self.res[2],width=25)
        self.tx2.place(x=300,y=150)

        self.lb3=Label(self.lin,text="Email",font=('arial',15,'bold'),width=20).place(x=19,y=200)
        self.tx3=Label(self.lin,font=10,text=self.res[3],width=25)
        self.tx3.place(x=300,y=200)

        self.lb4=Label(self.lin,text="Number of Passenger",font=('arial',15,'bold'),width=20).place(x=19,y=250)
        self.tx4=Label(self.lin,font=10,text=self.res[4],width=25)
        self.tx4.place(x=300,y=250)

        self.lb5=Label(self.lin,text="Fare",font=('arial',15,'bold'),width=20).place(x=19,y=300)
        self.tx5=Label(self.lin,font=10,text=self.res[5],width=25)
        self.tx5.place(x=300,y=300)

        self.btn=Button(self.lin,text="Pay",command=self.ope,font=('arial',10,'bold'),width=12,bd=8,relief="raised").place(x=250,y=400)
    def ope(self):
        self.lin.destroy()
        os.system("python selectbank.py")
    def fetch_data(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            cur.execute("select fname,lname , phone, email,totseat,totfare from passenger ORDER BY loginDate DESC,loginTime DESC")
            self.res=cur.fetchone()
            self.name= self.res[0]+" "+self.res[1]
        except Exception as ex:
            messagebox.showerror("Warning", ex, parent=self.lin)
        con.close()
    #Buttons

if __name__ == "__main__":
    root = Tk()
    obj = payment(root)
    root.mainloop()
