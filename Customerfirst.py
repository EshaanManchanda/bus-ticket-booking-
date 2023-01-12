from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import random
value = random.randint(101, 550)


class customerclass:
    def __init__(self, root):
        pass

        self.root = root
        self.root.geometry("734x800")
        self.root.config(bg="orange")
        self.root.resizable(False, False)
        self.root.title("Welcome to the Ticketing Portal")

        # -------Vriable decleration-------------------------------------------------
        self.fnametxt = StringVar()
        self.lnametxt = StringVar()
        self.emailtxt = StringVar()
        self.contact = StringVar()
        self.from_From = StringVar()
        self.to_To = StringVar()
        self.passe = StringVar()
        self.g = StringVar()
        self.busclass = StringVar()
        self.location = ['Amaravati', 'Itanagar', 'Dispur', 'Patna', 'Raipur', 'Panaji', 'Gandhinagar', 'Chandigarh', 'Shimla', 'Ranchi', 'Bengaluru',
                         'Thiruvananthapuram', 'Bhopal', 'Mumbai', 'Imphal', 'Shillong', 'Aizawl', 'Kohima', 'Bhubaneswar', 'Chandigarh', 'Jaipur',
                         'Gangtok', 'Chennai', 'Hyderabad', 'Agartala', 'Lucknow', 'Dehradun', 'Kolkata']
        self.age = ['1', '2', '3', '4', '5', '6']
        self.adult = IntVar()
        self.child = IntVar()
        self.old = IntVar()
        self.meals = StringVar()
        self.feed = StringVar()

        self.frame1 = Frame(self.root, bd=10, relief="raised",
                            width=730, height=70).grid(row=0)
        self.lb1 = Label(self.frame1, text="Bus Ticketing Portal",
                         font=('Helvetica', 18, 'bold')).grid(row=0)

        # Customer Details

        self.frame2 = Frame(self.root, bd=10, relief="raised",
                            width=380, height=350).place(x=5, y=70)

        self.lb2 = Label(self.frame2, text="Customer Details", bd=5,
                         relief="raised", width=28, font=10).place(x=35, y=80)
        self.lb3 = Label(self.frame2, text="First_Name",
                         font=5).place(x=135, y=126)

        self.tx6 = Entry(self.frame2, font=20,
                         textvariable=self.fnametxt).place(x=85, y=150)

        self.lb4 = Label(self.frame2, text="Last_Name",
                         font=5).place(x=135, y=175)
        self.tx1 = Entry(self.frame2, font=20,
                         textvariable=self.lnametxt).place(x=85, y=200)

        self.lb4 = Label(self.frame2, text="E_Mail_ID",
                         font=5).place(x=140, y=225)
        self.tx2 = Entry(self.frame2, font=20,
                         textvariable=self.emailtxt).place(x=85, y=250)

        self.lb4 = Label(self.frame2, text="Contact",
                         font=5).place(x=152, y=275)
        self.tx2 = Entry(self.frame2, font=20,
                         textvariable=self.contact).place(x=85, y=300)

        self.bt = Button(self.frame2, text="Login", command=self.addCustomer,
                         font=20, width=10, bd=10, relief="raised").place(x=120, y=350)

        # ------------Bus type---------------------------------------------------------

        self.frame3 = Frame(self.root, bd=10, relief="raised",
                            width=380, height=280).place(x=5, y=420)
        self.lb3 = Label(self.frame3, text="Bus Type", bd=5,
                         relief="raised", font=10, width=30).place(x=18, y=430)

        self.g.set(" ")
        self.rdDD = Radiobutton(self.frame3, text="Double-Decker", font=10,
                                value="Double-Decker", variable=self.g).place(x=20, y=480)
        self.rdSD = Radiobutton(self.frame3, text="Single-Decker", font=10,
                                value="Single-Decker", variable=self.g).place(x=20, y=510)
        self.rdLF = Radiobutton(self.frame3, text="Low-Floor", font=10,
                                value="Low-Floor", variable=self.g).place(x=20, y=540)
        self.rdMB = Radiobutton(self.frame3, text="Mini-Bus", font=10,
                                value="Mini-Bus", variable=self.g).place(x=20, y=570)
        self.rdOT = Radiobutton(self.frame3, text="Open-Top", font=10,
                                value="Open-Top", variable=self.g).place(x=20, y=600)
        self.rdHB = Radiobutton(self.frame3, text="Hybrid-Bus", font=10,
                                value="Hybrid-Bus", variable=self.g).place(x=20, y=630)

        # CLASS

        self.busclass.set(" ")
        self.lb = Label(self.frame3, text="Class", font=(
            "bold", 18), relief="sunken").place(x=230, y=480)
        self.rdAC = Radiobutton(self.frame3, text="AC Class", font=10,
                                value="AC Class", variable=self.busclass).place(x=220, y=510)
        self.rdNAC = Radiobutton(self.frame3, text="Non-AC", font=10,
                                 value="Non-AC", variable=self.busclass).place(x=220, y=540)
        # --------Bus Route---------------------------------------------------------------------------------------------------

        self.frame4 = Frame(self.root, bd=10, relief="raised",
                            width=350, height=630).place(x=380, y=70)
        self.lb4 = Label(self.frame4, text="Bus Route", bd=5,
                         relief="raised", font=10, width=28).place(x=390, y=80)

        # from
        self.lb5 = Label(self.frame4, text="From", width=5,
                         font=10).place(x=510, y=115)
        self.from_From.set("Select Destination")
        self.dropFrom = OptionMenu(
            self.frame4, self.from_From, *self.location).place(x=480, y=140)

        # to
        self.lb6 = Label(self.frame4, text="To", width=5,
                         font=10).place(x=510, y=172)
        self.to_To.set("Select Destination")
        self.dropTo = OptionMenu(
            self.frame4, self.to_To, *self.location).place(x=480, y=195)


        # age
        self.lb8 = Label(self.frame4, text="Adult",
                         font=10).place(x=410, y=308)
        self.dropAdu = OptionMenu(
            self.frame4, self.adult, *self.age).place(x=410, y=350)

        self.lb9 = Label(self.frame4, text="Child",
                         font=10).place(x=510, y=308)
        self.dropchi = OptionMenu(
            self.frame4, self.child,*self.age).place(x=510, y=350)

        self.lb10 = Label(self.frame4, text="Old", font=10).place(x=620, y=308)
        self.dropold = OptionMenu(
            self.frame4, self.old,*self.age).place(x=610, y=350)

        # no of passenger
        self.lb7 = Label(self.frame4, text="Number of Passengers",
                         width=20, font=10).place(x=450, y=235)
        self.tx8 = Label(self.frame4, font=10,
                         text="0")
        self.tx8.place(x=450, y=265)
        # Meal
        # self.frame5=Frame(self.root,bd=10,relief="raised",width=350,height=280).place(x=380,y=420)
        self.meals.set(" ")
        self.lb11 = Label(self.frame4, text="Would you like Something?",
                          width=22, font=10).place(x=380, y=440)

        self.meal = Radiobutton(self.frame4, text="Want Meal", font=10,
                                variable=self.meals, value="Yes").place(x=510, y=470)
        self.nomeal = Radiobutton(self.frame4, text="No Meal", font=10,
                                  variable=self.meals, value="No").place(x=510, y=500)
        
        self.bt = Button(self.frame4, text="Submit",command=self.submit, bd=10,
                         relief="raised", font=10).place(x=500, y=620)
        self.update_content()

        # Reset
        # ---------------------------------------------------------------------------------------------
        def res():
            self.fnametxt.set("")
            self.lnametxt.set("")
            self.contact.set("")
            self.emailtxt.set("")
            self.adult.set("0")
            self.child.set("0")
            self.old.set("0")
            self.feed.set("")
            self.from_From.set("Select Destination")
            self.passe.set("")
            self.to_To.set("Select Destination")
        # ---------------------------------------------------------------------------------

        # 2nd Module
        # def new():
        #     if num1.get()=="" and num2.get()=="" and num3.get()=="" and num4.get()=="" and passe.get()=="" and feed.get()=="":
        #         messagebox.showerror("Error","Check all Credentials")
        #     else:
        #         messagebox.showinfo("Error","Welcome to Fare Page")

        #         root=Tk()
        #         root.geometry("800x750")
        #         root.title("Welcome To Bus Portal")
        #         root.config(bg="Red")
        #         root.resizable(False,False)

        #         fr=Frame(root,width=800,bd=10,height=50,relief="raised")
        #         fr.place(x=0,y=5)
        #         frlb=Label(fr,text="Fare Portal",font=('arial',15,'bold'),width=15)
        #         frlb.place(x=270,y=0)

        #         lb=Label(root,text="Bus Route",font=('arial',15,'bold'),width=20).place(x=19,y=100)
        #         fr=StringVar()
        #         tx=Entry(root,font=10,textvariable=fr)
        #         tx.place(x=300,y=100)
        #         to=StringVar()
        #         tx2=Entry(root,font=10,textvariable=to)
        #         tx2.place(x=550,y=100)

        #         typ=StringVar()

        #         lb2=Label(root,text="Bus Type",font=('arial',15,'bold'),width=20).place(x=19,y=150)
        #         tx2=Entry(root,font=10,textvariable=typ).place(x=300,y=150)

        #         rn=StringVar()

        #         lb3=Label(root,text="Route Number",font=('arial',15,'bold'),width=20).place(x=19,y=200)
        #         tx =Entry(root,font=10,textvariable=rn).place(x=300,y=200)

        #         fare=StringVar()
        #         lb4=Label(root,text="Per Seat Fare",font=('arial',15,'bold'),width=20).place(x=19,y=250)
        #         text1=Label(root,text="",font=('arial',15,'bold'),textvariable=fare).place(x=300,y=250)

        #         nop=StringVar()
        #         lb5=Label(root,text="Number of Passenger",font=('arial',15,'bold'),width=20).place(x=19,y=300)
        #         text2=Label(root,text="",font=('arial',15,'bold'),textvariable=nop).place(x=300,y=300)

        #         tsf=StringVar()
        #         lb6=Label(root,text="Total Seat Fare",font=('arial',15,'bold'),width=20).place(x=19,y=350)
        #         tx7=Entry(root,font=10,textvariable=tsf).place(x=300,y=350)

        #         mc=StringVar()
        #         lb7=Label(root,text="Meal Cost",font=('arial',15,'bold'),width=20).place(x=19,y=400)
        #         tx8=Entry(root,font=10,textvariable=mc).place(x=300,y=400)

        #         tf=StringVar()
        #         lb8=Label(root,text="Total Fare",font=('arial',15,'bold'),width=20).place(x=19,y=450)
        #         tx9=Entry(root,font=10,textvariable=tf).place(x=300,y=450)

        #         tax=StringVar()
        #         tax.set("18%")
        #         lb9=Label(root,text="Tax",font=('arial',15,'bold'),width=20).place(x=19,y=500)
        #         tx10=Entry(root,font=10,textvariable=tax).place(x=300,y=500)

        #         tpf=StringVar()
        #         lb10=Label(root,text="Total Payble For",font=('arial',15,'bold'),width=20).place(x=19,y=550)
        #         tx10=Entry(root,font=10,textvariable=tpf).place(x=300,y=550)

        #         def clearb():
        #             qExit=messagebox.askyesno(" Quit System ", " Do you really want to cancel trip ? ")
        #             if qExit > 0:
        #                 root.destroy()
        #                 return
        #             else:
        #                 messagebox.showinfo("Message","Moving to Fare page")

        #         def tick():
        #             os.system("ticket3.py")#pay

        #         def close():
        #             root.destroy()         #re book
        #         btn=Button(root,text="Cancel Trip",font=('arial',10,'bold'),command=clearb,width=12,bd=8,relief="raised").place(x=50,y=650)
        #         btn=Button(root,text="Book",command=tick,font=('arial',10,'bold'),width=12,bd=8,relief="raised").place(x=250,y=650)
        #         btn=Button(root,text="Re-Book",command=close,font=('arial',10,'bold'),width=12,bd=8,relief="raised").place(x=450,y=650)

        # -------------------------------------------------------------------------------------------------
        btn4 = Button(self.root, text="Reset", font=10, bd=10,
                      relief="raised", width=15, command=res).place(x=40, y=720)
        # btn5=Button(self.root,text="Fare",command=new,font=10,bd=10,relief="raised",width=15).place(x=285,y=720)
        btn7 = Button(self.root, text="Exit", font=10, bd=10, relief="raised",
                      width=15, command=self.root.destroy).place(x=530, y=720)
    # ---------------All Funtions--------------------------------------------------------------

    def addCustomer(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            cur.execute("select * from passenger where phone=?", (self.contact.get(),))
            row=cur.fetchone()
            if row!=None:
                    op=messagebox.askyesno("Confirm","Your contact no. already exist , do you want to restore",parent=self.root)
                    if op==True:
                        self.fnametxt.set(row[1])
                        self.lnametxt.set(row[2])
                        self.contact.set(row[3])
                        self.emailtxt.set(row[4])
                        self.from_From.set(row[5])
                        self.to_To.set(row[6])
                        # self.passe.set(row[7])
                        self.g.set(row[11])
                        self.busclass.set(row[17])
                        if row[8]==None:
                            self.adult.set("0")
                        else:
                            self.adult.set(int(row[8]))
                        if row[9]==None:
                            self.child.set("0")
                        else:
                            self.child.set(int(row[9]))

                        if row[10]==None:
                            self.old.set("0")
                        else:
                            self.old.set(int(row[10]))
                        self.feed.set(row[18])
                        return
            elif self.fnametxt.get() == "" or self.lnametxt.get() == "" or self.contact.get() == "" or self.emailtxt == "":
                messagebox.showerror(
                    "Warning", "Please submit all crediantials", parent=self.root)
            else:
                
                if len(self.contact.get()) ==11:
                    messagebox.showerror("Warning","Please check you phone number", parent=self.root)
                else:
                    cur.execute("insert into passenger(fname,lname,phone,email) values('"+self.fnametxt.get(
                        )+"','"+self.lnametxt.get()+"','"+self.contact.get()+"','"+self.emailtxt.get()+"')")
                    con.commit()
                    messagebox.showinfo("Message", "Data Submitted", parent=self.root)
            # cur.execute("delete from passenger where fname='Eshaan' ")
            # con.commit()
        except Exception as ex:
            messagebox.showerror("error", ex, parent=self.root)
        con.close()
    # def submit_all():
    #     fro=from_From.get()
    #     too=to_To.get()
    #     passen=passe.get()
    #     agea=age_adult.get()
    #     nomeal=feed.get()
    #     agec=child.get()
    #     ageo=old.get()
    #     try:
    #         conn = pymysql.connect(host='localhost',user='root',password='123456',db='ticketing')
    #         mydb=conn.cursor()
    #         mydb.execute("insert into passenger(fromD,toD,nbseats,nrseats,noofmeals,childnrseats,oldnrseats) values('"+fro+"','"+too+"','"+passen+"','"+agea+"','"+nomeal+"','"+agec+"','"+ageo+"')")
    #         conn.commit()
    #         messagebox.showinfo("Message","Destination Submitted")
    #     except:
    #         conn.rollback()
    #         messagebox.showerror("Message","Destination not Submitted")
    #     conn.close()

    def submit(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            if self.busclass.get() == "" or self.g.get() == "":
                messagebox.showerror(
                    "Warning", "Please submit all crediantials", parent=self.root)
            else:
                cur.execute("select * from passenger where phone=?", (self.contact.get(),))
                row=cur.fetchone()
                if row!=None:
                    cur.execute("update passenger set type=?,class=?,aduseat=?, chiseat=?,oldseat=?, totseat=?, fromD=? , toD=? where phone=?",(self.g.get(),self.busclass.get(),self.adult.get(),self.child.get(),self.old.get(),self.passe,self.from_From.get(), self.to_To.get(),self.contact.get()))
                    con.commit()
                    messagebox.showinfo("Message","Data Submitted",parent=self.root)
                else:
                    messagebox.showerror("Warning","Please login first , if you login already just add you contact number.",parent=self.root)
        except Exception as ex:
            # con.rollback()
            messagebox.showerror("Message",ex,parent=self.root)
        con.close()
    def update_content(self):

        self.passe=self.adult.get()+self.old.get()+self.child.get()
        # print(self.passe)
        self.tx8.config(text=f"{str(self.passe)}")
        print(self.meals)
        if self.meals=="Yes":
            self.lb12 = Label(self.frame4, text="Number of Meals:",
                            font=20, width=15).place(x=380, y=535)

            self.tx5 = Entry(self.frame4, width=20, font=20,
                            textvariable=self.feed).place(x=450, y=576)
        self.tx8.after(1000,self.update_content)



if __name__ == "__main__":
    root = Tk()
    obj = customerclass(root)
    root.mainloop()
