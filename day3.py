import tkinter
from tkinter import*

import tkinter as tk
from tkinter import ttk, Radiobutton

import txt as txt
import violet as violet


def getvls():
    print("youre form submitted")


root = Tk()
# Declaring Window Title
root.title("Registration form")
Label(root,text="Registraion Form",font="aerial 15 bold").grid(row=0,column=3)
# Declaring Window size
root.geometry('560x460')
# Declaring Window Color
root.configure(background="white")
# below four fields are declared
name = Label(root,text ="Name")
gender = Label(root,text ="Gender")
email = Label(root,text ="Email")
phoneno = Label(root,text ="Phone no")
# packing field
name.grid(row=1,column=1)
gender.grid(row=2,column=1)
email.grid(row=3,column=1)
phoneno.grid(row=4,column=1)
# storing varible
namevalue = StringVar
gendervalue = StringVar
emailvalue = StringVar
phonenovalue = StringVar
var = IntVar()
#creating entry field
nameentry = Entry(root,textvariable=namevalue)

emailentry = Entry(root,textvariable=emailvalue)
phonenoentry = Entry(root,textvariable=phonenovalue)
#packing entry field
nameentry.grid(row=1,column=3)

emailentry.grid(row=3,column=3)
phonenoentry.grid(row=4,column=3)

btn = ttk.Button(root,text="Submit",bg=violet,command=getvls).grid(row=5,column=1)


def getsel():
    selection = str(var.get())
    Label.config(text=selection)

Radiobutton1 = Radiobutton(root, text="male",variable = var,value=1,command =getsel)
Radiobutton1.grid(row = 2,column = 3)


Radiobutton2 = Radiobutton(root, text="female",variable = var,value=2,command =getsel)
Radiobutton2.grid(row = 2,column = 4)

root.mainloop()