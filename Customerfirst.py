from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import random
value = random.randint(101, 550)


class customerclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("734x800")
        self.root.config(bg="orange")
        self.root.resizable(False, False)
        self.root.title("Welcome to the Ticketing Portal")
        self.root.focus_force()

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
        self.feed = IntVar()
        self.fare_opt = IntVar()
        self.fare_opt = 0

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
            self.frame4, self.child, *self.age).place(x=510, y=350)

        self.lb10 = Label(self.frame4, text="Old", font=10).place(x=620, y=308)
        self.dropold = OptionMenu(
            self.frame4, self.old, *self.age).place(x=610, y=350)

        # no of passenger
        self.lb7 = Label(self.frame4, text="Number of Passengers",
                         width=20, font=10).place(x=450, y=235)
        self.tx8 = Label(self.frame4, font=10,
                         text=f"0")
        self.tx8.place(x=450, y=265)
        # Meal
        # self.frame5=Frame(self.root,bd=10,relief="raised",width=350,height=280).place(x=380,y=420)
        self.meals.set(None)
        self.lb11 = Label(self.frame4, text="Would you like Something?",
                          width=22, font=10).place(x=380, y=440)

        self.meal = Radiobutton(self.frame4, text="Want Meal", font=10,
                                variable=self.meals, value=1)
        self.meal.place(x=510, y=470)
        self.nomeal = Radiobutton(self.frame4, text="No Meal", font=10,
                                  variable=self.meals, value=0)
        self.nomeal.place(x=510, y=500)

        self.lb12 = Label(self.frame4, text="Number of Meals:",
                          font=20, width=15)
        self.lb12.place(x=380, y=535)

        self.tx5 = Entry(self.frame4, width=20, font=20,
                         textvariable=self.feed)
        self.tx5.place(x=450, y=576)
        self.bt = Button(self.frame4, text="Submit", command=self.submit, bd=10,
                         relief="raised", font=10).place(x=500, y=620)
        btn4 = Button(self.root, text="Reset", font=10, bd=10,
                      relief="raised", width=15, command=self.res).place(x=40, y=720)
        self.fare_btn = Button(
            self.root, text="Fare", command=self.new, font=10, bd=10, relief="raised", width=15)
        self.fare_btn.place(x=285, y=720)
        btn7 = Button(self.root, text="Exit", font=10, bd=10, relief="raised",
                      width=15, command=self.root.destroy).place(x=530, y=720)
        self.update_content()
        # Reset
        # ---------------------------------------------------------------------------------------------

    def res(self):
        self.fnametxt.set("")
        self.lnametxt.set("")
        self.contact.set("")
        self.emailtxt.set("")
        self.adult.set("0")
        self.child.set("0")
        self.old.set("0")
        self.feed.set(0)
        self.from_From.set("Select Destination")
        # self.passe.set("")
        print(self.meals.get())
        self.to_To.set("Select Destination")

        
        
    # ---------------All Funtions--------------------------------------------------------------

    def addCustomer(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            cur.execute("select * from passenger where phone=?",
                        (self.contact.get(),))
            row = cur.fetchone()
            if row != None:
                op = messagebox.askyesno(
                    "Confirm", "Your contact no. already exist , do you want to restore", parent=self.root)
                if op == True:
                    self.fnametxt.set(row[1])
                    self.lnametxt.set(row[2])
                    self.contact.set(row[3])
                    self.emailtxt.set(row[4])
                    self.from_From.set(row[5])
                    self.to_To.set(row[6])
                    # self.passe.set(row[7])
                    self.g.set(row[11])
                    self.busclass.set(row[17])
                    if row[8] == None:
                        self.adult.set("0")
                    else:
                        self.adult.set(int(row[8]))
                    if row[9] == None:
                        self.child.set("0")
                    else:
                        self.child.set(int(row[9]))

                    if row[10] == None:
                        self.old.set("0")
                    else:
                        self.old.set(int(row[10]))
                    if row[18] != None and row[18] != "0":
                        self.meals.set("1")
                        self.feed.set(int(row[18]))
                    else:
                        self.feed.set(0)
                        self.meals.set(0)
                    return
            elif self.fnametxt.get() == "" or self.lnametxt.get() == "" or self.contact.get() == "" or self.emailtxt == "":
                messagebox.showerror(
                    "Warning", "Please submit all crediantials", parent=self.root)
            else:

                if len(self.contact.get()) < 10 or len(self.contact.get()) >= 11:
                    messagebox.showerror(
                        "Warning", "Please check you phone number", parent=self.root)
                else:
                    cur.execute("insert into passenger(fname,lname,phone,email) values('"+self.fnametxt.get(
                    )+"','"+self.lnametxt.get()+"','"+self.contact.get()+"','"+self.emailtxt.get()+"')")
                    con.commit()
                    messagebox.showinfo(
                        "Message", "Data Submitted", parent=self.root)
            print(len(self.contact.get()))
            # cur.execute("delete from passenger")
            # con.commit()
        except Exception as ex:
            messagebox.showerror("error", ex, parent=self.root)
        con.close()

    def submit(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        try:
            if self.busclass.get() == "" or self.g.get() == "" or self.passe == 0 or self.from_From.get() == "Select Destination" or self.to_To.get() == "Select Destination":
                messagebox.showerror(
                    "Warning", "Please submit all crediantials", parent=self.root)
            else:
                cur.execute("select * from passenger where phone=?",
                            (self.contact.get(),))
                row = cur.fetchone()
                if row != None:
                    if self.from_From.get() == self.to_To.get():
                        messagebox.showerror(
                            "Warning", "You destination should be different!!!!", parent=self.root)
                    else:
                        if self.meals.get() == "1":
                            cur.execute("update passenger set type=?,class=?,aduseat=?, chiseat=?,oldseat=?, totseat=?, fromD=? , toD=?,noofmeals=? where phone=?", (self.g.get(
                            ), self.busclass.get(), self.adult.get(), self.child.get(), self.old.get(), self.passe, self.from_From.get(), self.to_To.get(), self.feed.get(), self.contact.get()))
                            con.commit()
                            messagebox.showinfo(
                                "Message", "Data Submitted", parent=self.root)
                            self.fare_opt = 1
                        elif self.meals.get() == "0":
                            feed = 0
                            cur.execute("update passenger set type=?,class=?,aduseat=?, chiseat=?,oldseat=?, totseat=?, fromD=? , toD=?,noofmeals=? where phone=?", (self.g.get(
                            ), self.busclass.get(), self.adult.get(), self.child.get(), self.old.get(), self.passe, self.from_From.get(), self.to_To.get(), feed, self.contact.get()))
                            con.commit()
                            messagebox.showinfo(
                                "Message", "Data Submitted", parent=self.root)
                            self.fare_opt = 1
                        else:
                            messagebox.showerror(
                                "Warning", "Please select meal", parent=self.root)

                else:
                    messagebox.showerror(
                        "Warning", "Please login first , if you login already just add you contact number.", parent=self.root)
        except Exception as ex:
            # con.rollback()
            messagebox.showerror("Message", ex, parent=self.root)
        con.close()

    def update_content(self):

        self.passe = self.adult.get()+self.old.get()+self.child.get()
        # print(self.passe)
        self.tx8.config(text=f"{str(self.passe)}")
        if self.meals.get() == '1':
            self.tx5.config(state=NORMAL)
            self.lb12['state'] = NORMAL
        else:
            self.tx5.config(state=DISABLED)
            self.lb12['state'] = DISABLED
        # print(self.fare_opt)
        if self.fare_opt == 1:
            self.fare_btn.config(state=NORMAL)
        else:
            self.fare_btn.config(state=DISABLED)
        self.tx8.after(1000, self.update_content)
# ---------------------------------------------------------------------------------

        # 2nd Module
    def new(self):
        self.fareWin = Toplevel(self.root)
        self.root.withdraw()
        self.fareWin.geometry("800x750")
        self.fareWin.title("Welcome To Bus Portal")
        self.fareWin.config(bg="Red")
        self.fareWin.resizable(False, False)
        self.fareWin.focus_force()

        # self.fr = StringVar()
        # self.to = StringVar()
        # self.typ = StringVar()
        self.rn = StringVar()
        self.fare = StringVar()
        self.mc = IntVar()
        try:
            con = sqlite3.connect(database=r'ticketing.db')
            cur = con.cursor()
            cur.execute("select * from bus where fromD=? and toD=?",(self.from_From.get(),self.to_To.get()))
            res=cur.fetchall()
            print(res)
        except Exception as ex:
            messagebox.showerror("Message", ex, parent=self.fareWin)

        self.fr = Frame(self.fareWin, width=800, bd=10,
                        height=50, relief="raised")
        self.fr.place(x=0, y=5)
        self.frlb = Label(self.fr, text="Fare Portal",
                          font=('arial', 15, 'bold'), width=15)
        self.frlb.place(x=270, y=0)


        self.lb = Label(self.fareWin, text="Bus Route", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=100)
        self.tx = Label(self.fareWin, font=10, text=self.from_From.get(),width=20)
        self.tx.place(x=300, y=100)
        self.tx2 = Label(self.fareWin, font=10, text=self.to_To.get(),width=20)
        self.tx2.place(x=550, y=100)


        self.lb2 = Label(self.fareWin, text="Bus Type", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=150)
        self.tx2 = Label(self.fareWin, font=10,
                         text=self.g.get(),width=20).place(x=300, y=150)


        self.lb3 = Label(self.fareWin, text="Route Number", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=200)
        self.tx = Label(self.fareWin, font=10,
                        text=value,width=20).place(x=300, y=200)

        self.lb4 = Label(self.fareWin, text="Per Seat Fare", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=250)
        self.text1 = Label(self.fareWin, font=(
            'arial', 15, 'bold'), text=self.fare).place(x=300, y=250)

        self.nop = StringVar()
        self.lb5 = Label(self.fareWin, text="Number of Passenger", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=300)
        self.text2 = Label(self.fareWin, text=self.passe, font=(
            'arial', 15, 'bold'), width=20).place(x=300, y=300)

        self.tsf = StringVar()
        self.lb6 = Label(self.fareWin, text="Total Seat Fare", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=350)
        self.tx7 = Entry(self.fareWin, font=10,
                         textvariable=self.tsf).place(x=300, y=350)

        self.lb7 = Label(self.fareWin, text="Meal Cost", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=400)
        self.tx8 = Entry(self.fareWin, font=10,
                         textvariable=self.mc).place(x=300, y=400)

        self.tf = StringVar()
        self.lb8 = Label(self.fareWin, text="Total Fare", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=450)
        self.tx9 = Entry(self.fareWin, font=10,
                         textvariable=self.tf).place(x=300, y=450)

        self.tax = StringVar()
        self.tax.set("18%")
        self.lb9 = Label(self.fareWin, text="Tax", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=500)
        self.tx10 = Entry(self.fareWin, font=10,
                          textvariable=self.tax).place(x=300, y=500)

        self.tpf = StringVar()
        self.lb10 = Label(self.fareWin, text="Total Payble For", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=550)
        self.tx10 = Entry(self.fareWin, font=10,
                          textvariable=self.tpf).place(x=300, y=550)
        self.btn = Button(self.fareWin, text="Cancel Trip", font=(
            'arial', 10, 'bold'), command=self.clearb, width=12, bd=8, relief="raised").place(x=50, y=650)
        self.btn = Button(self.fareWin, text="Book", command=self.tick, font=(
            'arial', 10, 'bold'), width=12, bd=8, relief="raised").place(x=250, y=650)
        # self.btn = Button(self.fareWin, text="Re-Book", command=self.lose, font=(
        #     'arial', 10, 'bold'), width=12, bd=8, relief="raised").place(x=450, y=650)

    def clearb(self):
        qExit = messagebox.askyesno(
            " Quit System ", " Do you really want to cancel trip ? ")
        if qExit > 0:
            self.root.destroy()
            os.system("python Customerfirst.py")
            return 
        else:
            messagebox.showinfo("Message", "Moving to Fare page")

    def tick(self):
        self.fareWin.destroy()
        os.system("ticket3.py")  # pay

    def close(self):
        self.root.destroy()
        os.system(" python Customerfirst.py") # re book

        # -------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    root = Tk()
    obj = customerclass(root)
    root.mainloop()
