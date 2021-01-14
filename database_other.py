from tkinter import *
from functools import partial
import tkinter as tk
import sqlite3

class LoginGUI(tk.Tk):
    def __init__(self, app):
        self.app=app
        app.title('Database login')
        app.geometry("600x600")

        self.first_l=Label(self.app,text='First name')
        self.first_l.grid(row=0,column=0,ipadx=50)
        self.first_e=Entry(self.app, width=30)
        self.first_e.grid(row=0,column=1)

        self.last_l=Label(self.app,text='Last name')
        self.last_l.grid(row=1,column=0)
        self.last_e=Entry(self.app, width=30)
        self.last_e.grid(row=1,column=1)

        self.email_l=Label(self.app,text='Email')
        self.email_l.grid(row=2,column=0)
        self.email_e=Entry(self.app, width=30)
        self.email_e.grid(row=2,column=1)

        self.address_l=Label(self.app,text='Address')
        self.address_l.grid(row=3,column=0)
        self.address_e=Entry(self.app, width=30)
        self.address_e.grid(row=3,column=1)

        self.delete_box=Entry(root, width=30)
        self.delete_box.grid(row=8, column=1)
        self.delete_box_l=Label(root, text='ID number')
        self.delete_box_l.grid(row=8, column=0)

        self.enter_button=Button(self.app, text='Enter Info',command=self.submit)
        self.enter_button.grid(row=4,column=0, columnspan=2, pady=10, padx=60, ipadx=211)

        self.enter_button=Button(self.app, text='Show Records',command=self.query)
        self.enter_button.grid(row=5,column=0, columnspan=2, pady=10, padx=60, ipadx=199)

        self.delete_button=Button(self.app, text='Delete Record',command=self.delete)
        self.delete_button.grid(row=7,column=0, columnspan=2, pady=10, padx=60, ipadx=200)
    def submit(self):
        #Connect to database
        conn=sqlite3.connect('Library_info.db')
        c=conn.cursor()
        c.execute("INSERT INTO addresses VALUES (:first, :last, :email, :address)",
                {
                    'first':self.first_e.get(),
                    'last':self.last_e.get(),
                    'email':self.email_e.get(),
                    'address':self.address_e.get()
                })
        conn.commit()
        conn.close()
        #Clear text
        self.first_e.delete(0,END)
        self.last_e.delete(0,END)
        self.email_e.delete(0,END)
        self.address_e.delete(0,END)

    def query(self):
        conn=sqlite3.connect('Library_info.db')
        c=conn.cursor()
        c.execute("SELECT *, oid FROM addresses")
        records= c.fetchall()

        print_records=''
        for record in records:
            print_records+=str(record[0:2]) +' ' + str(record[4])+'\n'

        query_label=Label(root,text=print_records)
        query_label.grid(row=6, column=0, columnspan=2)

        conn.commit()
        conn.close()

    def delete(self):
        conn=sqlite3.connect('Library_info.db')
        c=conn.cursor()

        c.execute("DELETE from addresses WHERE oid="+self.delete_box.get())
        self.delete_box.delete(0, END)
        conn.commit()
        conn.close()
root=Tk()
example=LoginGUI(root)
root.mainloop()
