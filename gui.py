from tkinter import *
import tkinter.messagebox
window = tkinter.Tk()
window.title("Student Details")

def sel():
    selection = "You selected the option "+ str(user.get())
    print(selection)

def Sign_InAction():
    tkinter.messagebox.showinfo("Alert Message","This a basic alert!!!")

tkinter.Label(window,text = "Username").grid(row=0)

username=tkinter.Entry(window).grid(row=0,column=1)
user=IntVar()

r1=Radiobutton(window,text="student",variable=user,value=1,command=sel)
r2=Radiobutton(window,text="admin",variable=user,value=1,command=sel)
r1.grid(row=2)
r2.grid(row=2,column=1)

tkinter.Checkbutton(window,text="Keep me Loged In").grid(columnspan = 2)

tkinter.Button(window,text="Sign in",command=Sign_InAction()).grid(row=4,columnspan=4)

window.mainloop()

    
