from tkinter import *
from functools import partial
import tkinter as tk

class Node(object):
    """
    Represents a singly-linked node
    """
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

class LinkedList(object):
    """
    Represents a singly-linked list
    """
    def __init__(self):
        self.head = None

class LoginSystemChaining(object):
    """
    Represents a hash table the stores usernames and passwords using separate
    chaining
    """
    def __init__(self, size):
        """
        size: int, positive integer
        """
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append(LinkedList())

system=LoginSystemChaining(100)

class LoginGUI(tk.Tk):
    def __init__(self, app):
        self.app=app
        app.title('Database login')
        app.geometry("400x300")

        self.first_l=Label(self.app,text='First name')
        self.first_l.grid(row=0,column=0)
        self.first_e=Entry(self.app)
        self.first_e.grid(row=0,column=1)

        self.last_l=Label(self.app,text='Last name')
        self.last_l.grid(row=1,column=0)
        self.last_e=Entry(self.app)
        self.last_e.grid(row=1,column=1)

        self.enter_button=Button(self.app, text='Enter',command=self.submit)
        self.enter_button.grid(row=1,column=2)


    def close_app(self):
        self.destroy()

    def submit(self):
        #function takes entry from user for first and last name and checks database
        #to see if the user is already in the database; otherwise adds them to it
        first=self.first_e.get()
        last=self.last_e.get()
        self.first_e.delete(0,END)
        self.last_e.delete(0,END)
        firstlast=first.lower()+last.lower()

        userID=0
        for char in firstlast:
            userID+=ord(char)
        hashedID=userID%100

        lst=system.table[hashedID]
        curr=lst.head
        while curr is not None:
            if curr.value==firstlast:
                print('User is a member of the database')
                return True
            curr=curr.next
        new_node=Node(firstlast,lst.head)
        lst.head=new_node
        print('User was added to the database')
        return False


root=Tk()
example=LoginGUI(root)
root.mainloop()
