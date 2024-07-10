from tkinter import *
from typing import Sized
root=Tk()
root.geometry("700x200")
Label(root, text="Dance Academy Form", font="PerpetuaTitlingMT 25 bold underline", pady=4, padx=25, fg="white", bg="black", relief=SUNKEN).grid(row=5,column=5)

name = Label(root, text="Name: ").grid(row=18)
dob = Label(root, text="DOB: ").grid(row=19)
age = Label(root, text="Age: ").grid(row=20)

namevalue=StringVar()
dobvalue=StringVar()
agevalue=StringVar()

nameEntry=Entry(root,textvariable=namevalue)
dobEntry=Entry(root,textvariable=dobvalue)
ageEntry=Entry(root,textvariable=agevalue)

nameEntry.grid(row=18, column=1)
dobEntry.grid(row=19, column=1)
ageEntry.grid(row=20, column=1)

def save():
    f = open("form.txt", "a")
    f.write(f"Name: {namevalue.get()}\n")
    f.write(f"DOB: {dobvalue.get()}\n")
    f.write(f"Age: {agevalue.get()}\n\n")
    f.close()
    root.destroy()

Button(root, text="Submit", command=save).grid(column=1)
root.mainloop()