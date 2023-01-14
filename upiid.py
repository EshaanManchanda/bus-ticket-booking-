import sqlite3
import time
from tkinter import*
from tkinter import messagebox
import os
class upi:
    def __init__(self, root):
        self.win=root
        self.win.config(bg="#FCE6C9")
        self.win.geometry("620x450")
        self.win.title("UPI Payment")
        self.win.resizable(False,False)

        self.frame=Frame(self.win,bg='red4',bd=10,relief="raised",width=400,height=50).place(x=100,y=1)
        self.lb=Label(self.frame,bg='red4',fg='white',text="UPI ID",font=20).place(x=280,y=12)
        self.frame2=Frame(self.win,bd=10,relief="raised",width=600,height=350,bg="red4").place(x=5,y=80)

        self.frame3=Frame(self.win,bg='gold',bd=9,relief="raised",width=400,height=40).place(x=96,y=130)
        self.lb2=Label(self.frame3,bg='gold',fg='black',text="UPI Details",font=18).place(x=240,y=132)

        self.us=StringVar()
        self.lb=Label(self.frame2,bg='red4',fg='gold',text="UPI ID",font=20,width=10).place(x=150,y=200)
        self.pas=StringVar()
        self.lb2=Label(self.frame2,bg='red4',fg='gold',text="Password",font=20,width=10).place(x=140,y=250)

        self.tx=Entry(self.frame2,textvariable=self.us,font=10).place(x=250,y=200)
        self.tx2=Entry(self.frame2,textvariable=self.pas,font=10).place(x=250,y=250)

        self.btn=Button(self.frame2,bg='gold',fg='black',text="Submit",command=self.submit,font=20,bd=9,relief="raised",width=20).place(x=190,y=320)

    def submit(self):
        con = sqlite3.connect(database=r'ticketing.db')
        cur = con.cursor()
        if self.us.get()==""or self.pas.get()=="":
            messagebox.showerror("warning","Please fill all details",parent=self.win)
        else:
            try:
                value='upi'
                cur.execute("select * from passenger ORDER BY loginDate DESC,loginTime DESC")
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
    obj = upi(root)
    root.mainloop()
