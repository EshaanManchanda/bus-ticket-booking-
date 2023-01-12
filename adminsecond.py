from tkinter import*
from tkinter import messagebox
import os
from PIL import ImageTk, Image

win=Tk()
win.config(bg="aqua")
win.geometry("600x300")
win.resizable(False,False)
load=Image.open('bus.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)


def dd():
    os.system("updatebus.py")

def ll():
    os.system("updatepassengers.py")


btn=Button(win,bg='gold',fg='black',text="Update Bus Details",font=('arial',15,'bold'),width=20,bd=10,relief="raised",command=dd).place(x=20,y=50)
btn=Button(win,bg='gold',fg='black',text="Update Passenger Details",font=('arial',15,'bold'),width=20,bd=10,relief="raised",command=ll).place(x=320,y=50)
btn=Button(win,bg='gold',fg='black',text="Update Meal Details",font=('arial',15,'bold'),width=20,bd=10,relief="raised").place(x=320,y=170)
btn=Button(win,bg='gold',fg='black',text="Exit",font=('arial',15,'bold'),width=20,bd=10,relief="raised",command=win.destroy).place(x=20,y=170)
win.mainloop()
