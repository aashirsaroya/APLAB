from tkinter import *
import tkinter.messagebox
import sqlite3 as s
conn = s.connect("meradb.db")
conn.execute("""CREATE TABLE IF NOT EXISTS CUST(
NAME TEXT PRIMARY KEY,
AGE INT NOT NULL
)""")

window = tkinter.Tk()
window.title("Customer Details")
tkinter.Label(window,text='Name: ').grid(row=0)
str = StringVar()
age = StringVar()
tkinter.Entry(window,textvariable=str).grid(row=0,column=1)
tkinter.Label(window,text='Age: ').grid(row=1)
tkinter.Entry(window,textvariable=age).grid(row=    1,column=1)
def insert():
    conn.execute("INSERT INTO CUST(NAME,AGE) VALUES(",str.get(),',',age.get(),');')
    tkinter.messagebox.showinfo("Alert","Insertion Successful")
tkinter.Button(window,text='Ok',command=insert).grid(row=2,column=1)

window.mainloop()
