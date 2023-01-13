def new(self):
        self.fareWin = Toplevel(self.root)
        self.root.withdraw()
        self.fareWin.geometry("800x750")
        self.fareWin.title("Welcome To Bus Portal")
        self.fareWin.config(bg="Red")
        self.fareWin.resizable(False, False)
        self.fareWin.focus_force()

        self.fr = Frame(self.fareWin, width=800, bd=10,
                        height=50, relief="raised")
        self.fr.place(x=0, y=5)
        self.frlb = Label(self.fr, text="Fare Portal",
                          font=('arial', 15, 'bold'), width=15)
        self.frlb.place(x=270, y=0)

        self.lb = Label(self.fareWin, text="Bus Route", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=100)
        self.fr = StringVar()
        self.tx = Entry(self.fareWin, font=10, textvariable=self.fr)
        self.tx.place(x=300, y=100)
        self.to = StringVar()
        self.tx2 = Entry(self.fareWin, font=10, textvariable=self.to)
        self.tx2.place(x=550, y=100)

        self.typ = StringVar()

        self.lb2 = Label(self.fareWin, text="Bus Type", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=150)
        self.tx2 = Entry(self.fareWin, font=10,
                         textvariable=self.typ).place(x=300, y=150)

        self.rn = StringVar()

        self.lb3 = Label(self.fareWin, text="Route Number", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=200)
        self.tx = Entry(self.fareWin, font=10,
                        textvariable=self.rn).place(x=300, y=200)

        self.fare = StringVar()
        self.lb4 = Label(self.fareWin, text="Per Seat Fare", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=250)
        self.text1 = Label(self.fareWin, text="", font=(
            'arial', 15, 'bold'), textvariable=self.fare).place(x=300, y=250)

        self.nop = StringVar()
        self.lb5 = Label(self.fareWin, text="Number of Passenger", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=300)
        self.text2 = Label(root, text="", font=(
            'arial', 15, 'bold'), textvariable=self.nop).place(x=300, y=300)

        self.tsf = StringVar()
        self.lb6 = Label(self.fareWin, text="Total Seat Fare", font=(
            'arial', 15, 'bold'), width=20).place(x=19, y=350)
        self.tx7 = Entry(self.fareWin, font=10,
                         textvariable=self.tsf).place(x=300, y=350)

        self.mc = StringVar()
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
