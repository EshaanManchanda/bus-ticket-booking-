import sqlite3
import time
from tkinter import*
from tkinter import messagebox
import os
class debitcard:
    def __init__(self, root):
        self.win=root
        self.win.config(bg="cornsilk1")
        self.win.geometry("620x450")
        self.win.resizable(False,False)

        self.frame=Frame(self.win,bg='#808A87',bd=10,relief="raised",width=400,height=50).place(x=100,y=1)
        self.lb=Label(self.frame,bg='#808A87',fg='white',text="Debit Card",font=25).place(x=260,y=10)
        self.frame2=Frame(self.win,bd=10,relief="raised",width=600,height=350,bg="cornflowerblue").place(x=10,y=70)

        self.us=StringVar()
        self.lb=Label(self.frame2,text="Card Number",font=20,width=15).place(x=110,y=200)
        self.pas=StringVar()
        self.lb2=Label(self.frame2,text="Name",font=20,width=15).place(x=110,y=250)

        self.tx=Entry(self.frame2,textvariable=self.us,font=1).place(x=300,y=200)
        self.tx2=Entry(self.frame2,textvariable=self.pas,font=1).place(x=300,y=250)

        self.frame3=Frame(self.win,bg='orange',bd=9,relief="raised",width=400,height=40).place(x=96,y=130)
        self.lb2=Label(self.frame3,bg='orange',fg='black',text="Card Details",font=20).place(x=250,y=133)


        self.btn=Button(self.frame2,bg='orange',text="Submit",command=self.submit,font=20,bd=9,relief="raised",width=20).place(x=190,y=300)
    def submit(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        if self.us.get()==""or self.pas.get()=="":
            messagebox.showerror("warning","Please fill all details",parent=self.win)
        else:
            try:
                value='debit card'
                cur.execute("select pid from passenger ORDER BY loginDate DESC,loginTime DESC")
                res1=cur.fetchone()
                self.bookingid=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
                cur.execute("update passenger set pstatus=? ,bookingid=? where pid=?",(value,self.bookingid,res1[0]))
                con.commit()
                cur.execute("select * from passenger ORDER BY loginDate DESC,loginTime DESC")
                res=cur.fetchone()
                cur.execute("select * from Confirmbooking where pid=?",(res[0],))
                show=cur.fetchone()
                if show == None:
                    cur.execute("insert into Confirmbooking values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17],res[18],res[19],res[20],res[21]))
                    con.commit()
                cur.execute("delete from passenger where pid=?",(res[0],))
                con.commit()
            except Exception as ex:
                messagebox.showerror("Error",ex,parent=self.win)
            messagebox.showinfo("Successfully","payment done successfully",parent=self.win)
            self.win.destroy()
            os.system("python printticket.py")
        con.close()
if __name__ == "__main__":
    root = Tk()
    obj = debitcard(root)
    root.mainloop()

